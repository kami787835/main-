from django.db import models
import json

class File(models.Model):
    file_id = models.CharField(max_length=255, unique=True)  # Уникальный идентификатор файла
    file_name = models.CharField(max_length=255)  # Имя файла
    file_file = models.FileField(upload_to='banners/',null=True,blank=True)  # Путь для загрузки файла
    file_ext = models.CharField(max_length=10)  # Расширение файла
    file_date = models.DateTimeField(auto_now_add=True)  # Дата создания файла
    url = models.URLField()  # URL файла

    def __str__(self):
        return self.file_name

class Banner(models.Model):
    banner_id = models.CharField(max_length=255, unique=True)  # Уникальный идентификатор баннера
    banner_key = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Ключ баннера
    banner_title = models.CharField(max_length=255)  # Заголовок баннера
    banner_link = models.URLField(null=True,blank=True)  # Ссылка на баннер
    banner_visible = models.BooleanField(default=True)  # Статус видимости баннера
    banner_date_start = models.DateTimeField()  # Дата начала показа баннера
    banner_date_stop = models.DateTimeField(null=True,blank=True)  # Дата окончания показа баннера
    banner_date = models.DateTimeField(auto_now_add=True)  # Дата создания записи
    banner_data = models.JSONField()  # Дополнительные данные о баннере в формате JSON
    views = models.PositiveIntegerField(default=0)  # Количество просмотров

    # Связь с файлами (изображениями)
    files = models.ManyToManyField(File, related_name='banners', blank=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ['banner_date_start']  # Сортировка по дате начала

    def __str__(self):
        return self.banner_title

    def get_banner_images(self):
        """Метод для получения изображений баннера в виде словаря."""
        images_data = json.loads(self.banner_data)  # Декодируем данные
        images = {
            'mobile': images_data.get('mobile', {}),
            'tablet': images_data.get('tablet', {}),
            'desktop': images_data.get('desktop', {}),
            'desktop_topic': images_data.get('desktop_topic', {}),
        }
        return images
