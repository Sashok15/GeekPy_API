from my_api.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from my_api.config import CATEGORIES, URL_FOR_ALL
from my_api.mail_custom import send_email
from my_api.parse_save_data import *
import time


@api_view(['GET', 'POST'])
def api_parse_category(request, category_name):
    if request.method == 'GET':
        if category_name in CATEGORIES:
            start = time.time()
            data_list, amount = add_items_in_category_list(
                parse_category(URL_FOR_ALL.format(category_name))
            )
            save_in_db(category_name, data_list)
            end = time.time()
            _time = end - start
            elapsed_time = time.strftime("%H:%M:%S", time.gmtime(_time))
            send_email(amount, elapsed_time, category_name)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        content = {'error': 'Post method, need Get method '}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_view_list_category(request, category_name):
    if request.method == 'GET':
        if category_name in CATEGORIES:
            articles = Article.objects.filter(category_id__name=category_name)
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def api_view_detail_category(request, category_name, id_article):
    if request.method == 'GET':
        if category_name in CATEGORIES:
            try:
                article = Article.objects.filter(category_id__name=category_name) \
                    .filter(id_article=id_article)
                serializer = ArticleSerializer(article, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Article.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        content = {'error': 'need GET method'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
