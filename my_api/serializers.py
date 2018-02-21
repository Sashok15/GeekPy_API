from rest_framework import serializers
from my_api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id_article', 'title', 'text', 'time', 'descendants',
                  'by', 'kids', 'type', 'score', 'url', 'category_id')
