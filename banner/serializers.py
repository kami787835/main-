from rest_framework import serializers
from .models import File, Banner

class FileSerializer(serializers.ModelSerializer):
    """Сериализатор для модели File."""
    
    class Meta:
        model = File
        fields = ['file_id', 'file_name', 'file_file', 'file_ext', 'file_date', 'url']

class BannerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Banner."""
    
    files = FileSerializer(many=True, read_only=True)  # Включаем файлы в сериализатор баннера

    class Meta:
        model = Banner
        fields = '__all__'


    # def validate(self, attrs):
    #     """
    #     Проверка на корректность данных.
    #     """
    #     if attrs['banner_date_stop'] <= attrs['banner_date_start']:
    #         raise serializers.ValidationError("Дата окончания должна быть позже даты начала.")

    #     if Banner.objects.filter(banner_key=attrs['banner_key']).exists():
    #         raise serializers.ValidationError("Баннер с таким ключом уже существует.")

    #     return attrs

        # fields = [
        #     'banner_id', 'banner_key', 'banner_title', 
        #     'banner_link', 'banner_visible', 'banner_date_start', 
        #     'banner_date_stop', 'banner_date', 'banner_data', 
        #     'views', 'files'
        # ]

    # def to_representation(self, instance):
    #     """Переопределяем метод to_representation для добавления изображений."""
    #     representation = super().to_representation(instance)
    #     representation['images'] = instance.get_banner_images()  # Добавляем изображения баннера
    #     return representation
