from django.db import models
from transliterate.utils import _

LANG_CHOICES = (
    ("KR", "кыргыз тили"),
    ("RU", "Русский язык")
)

class News(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='RU', max_length=255, null=True, blank=True)
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержание")
    category = models.CharField("Категория", max_length=100)
    views = models.PositiveIntegerField("Просмотры", default=0)
    publication_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "Спецпроекты"
        verbose_name_plural = "Спецпроекты"

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    article = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(_("Изображение"), upload_to='news_images/')
    title = models.CharField(_("Заголовок"), max_length=200)

    class Meta:
        verbose_name = _("Изображение Спецпроекты")
        verbose_name_plural = _("Изображения Спецпроекты")
