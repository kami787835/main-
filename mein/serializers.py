from rest_framework import serializers
from .models import NewsArticle, NewsArticleImage


class NewsArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticleImage
        fields = ['id', 'image', 'title']

class NewsArticleSerializer(serializers.ModelSerializer):
    images = NewsArticleImageSerializer(many=True, read_only=True)  # Добавьте это поле

    class Meta:
        model = NewsArticle
        fields = ['id', 'language', 'title', 'content', 'category', 'views', 'publication_date', 'images']

