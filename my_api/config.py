# path
PATH_FOLDER = "reports"
PATH_LOGGING = "reports/hn_parser.log"
PATH_CSV = "reports/report.csv"
# parameters
CATEGORIES = ['askstories', 'showstories', 'newstories', 'jobstories']

# filsters
FROM_DATE = 1510852024
SCORE = 10

# url for requests
URL_FOR_ALL = 'https://hacker-news.firebaseio.com/v0/' \
              '{}.json?print=pretty'