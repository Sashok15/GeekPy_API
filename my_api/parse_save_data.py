import requests
import os
import logging
from my_api.config import PATH_FOLDER, PATH_LOGGING
from my_api.models import Category, Article

if not os.path.exists(PATH_FOLDER):
    os.makedirs(PATH_FOLDER)

logging.basicConfig(filename=PATH_LOGGING, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def parse_category(url_category):
    data = {}
    try:
        response = requests.get(url_category, timeout=10)
        data = response.json()
        return data

    except UnicodeEncodeError:
        logging.error('This is an error message. Unicode encode trouble. '
                      'Check data in request!!!')
    except Exception:
        logging.exception("Error in func  parse_category" + str(data), exc_info=True)


def add_items_in_category_list(for_category):
    category_info = []
    amount = 0
    for item in for_category:
        try:
            url = 'https://hacker-news.firebaseio.com/' \
                  'v0/item/' + str(item) + '.json?print=pretty'
            response = requests.get(url, timeout=10)
            item_info = response.json()
            # if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
            id = item_info['id']
            title = item_info['title']
            time = item_info['time']
            type = item_info['type']
            score = item_info['score']
            by = item_info['by']
            try:
                descendants = item_info['descendants']
            except KeyError:
                descendants = 'descendants'
            try:
                kids = item_info['kids']
            except KeyError:
                kids = 'kids'
            try:
                text = item_info['text']
            except KeyError:
                text = 'text'
            try:
                url = item_info['url']
            except KeyError:
                url = 'url'
            info = [id, title, time, descendants, by, kids, type, score, text, url]
            # print(info)
            amount += 1
            category_info.append(info)
        except Exception as e:
            logging.exception("Error in my func add_items", e)
    return category_info, amount


def update_create_data_category(category, item):
    if item[0] in Article.objects.values_list('id_article', flat=True):
        Article.objects.filter(id_article=item[0]).update(
            title=item[1], time=item[2],
            descendants=item[3], by=item[4], kids=item[5],
            type=item[6], score=item[7], text=item[8], url=item[9]
        )
    else:
        category.article_set.create(
            id_article=item[0], title=item[1], time=item[2],
            descendants=item[3], by=item[4], kids=item[5],
            type=item[6], score=item[7], text=item[8], url=item[9]
        )


def save_in_db(category_name, category_data):
    for item in category_data:
        # print(item)
        try:
            if category_name == 'askstories':
                category = Category.objects.get(id=1)
                update_create_data_category(category, item)

            elif category_name == 'showstories':
                category = Category.objects.get(id=2)
                update_create_data_category(category, item)

            elif category_name == 'newstories':
                category = Category.objects.get(id=3)
                update_create_data_category(category, item)

            elif category_name == 'jobstories':
                category = Category.objects.get(id=4)
                update_create_data_category(category, item)
            else:
                logging.info('False category in func /////save_in_db/////')
        except Exception as e:
            logging.exception('error', e)
