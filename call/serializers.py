from rest_framework import serializers
from .models import CallArticle, CallArticleImage

class CallArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallArticleImage
        fields = ['id', 'image', 'title']  # Укажите поля, которые хотите включить в сериализатор

class CallArticleSerializer(serializers.ModelSerializer):
    images = CallArticleImageSerializer(many=True, read_only=True)  # Вложенный сериализатор

    class Meta:
        model = CallArticle
        fields = ['id', 'language', 'title', 'content', 'category', 'views', 'publication_date', 'images']
