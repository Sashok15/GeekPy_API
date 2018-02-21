from django.conf.urls import url
from my_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'category/execute/(?P<category_name>\w{0,12})',
        views.api_parse_category),
    url(r'category/(?P<category_name>\w{0,12})/(?P<id_article>\d{0,9})',
        views.api_view_detail_category),
    url(r'category/(?P<category_name>\w{0,12})',
        views.api_view_list_category),

]
