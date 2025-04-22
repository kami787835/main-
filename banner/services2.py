from django.core.cache import cache
from django.utils import timezone
from .models import Banner
from django.utils import timezone
from django.core.cache import cache

def rotate_banners():
    """
    Выполнить ротацию баннеров, скрывая те, которые больше не должны отображаться.
    """
    now = timezone.now()  # Получаем текущее время
    banners_to_hide = Banner.objects.filter(banner_visible=True, banner_date_stop__lt=now)

    for banner in banners_to_hide:
        banner.banner_visible = False  # Устанавливаем статус видимости в False
        banner.save()  # Сохраняем изменения в базе данных

def get_next_banner():
    """
    Получить следующий активный баннер по порядку.
    """
    now = timezone.now()  # Получаем текущее время
    active_banners = Banner.objects.filter(
        banner_visible=True,
        banner_date_start__lte=now,
        banner_date_stop__gte=now
    ).order_by('banner_date_start')  # Сортируем по дате начала показа

    # Получаем индекс текущего баннера из кэша
    current_index = cache.get('current_banner_index', -1)

    if active_banners.exists():
        # Обновляем индекс для следующего запроса
        current_index = (current_index + 1) % active_banners.count()  # Циклический переход
        cache.set('current_banner_index', current_index, None)  # Обновляем индекс в кэше
        
        # Получаем баннер по новому индексу
        banner = active_banners[current_index]
        
        return banner  # Возвращаем текущий баннер
    return None  # Если активных баннеров нет, возвращаем None


def refresh_banners():
    """
    Обновить активные баннеры и скрыть устаревшие.
    """
    rotate_banners()  # Сначала выполняем ротацию баннеров
    cache.delete('current_banner_index')  # Сбрасываем индекс кэша
