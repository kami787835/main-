from .models import Banner
from django.utils import timezone
from django.core.cache import cache


def get_active_banners():
    """
    Получить все активные баннеры.
    """
    now = timezone.now()  # Получаем текущее время
    active_banners = Banner.objects.filter(
        banner_visible=True,
        banner_date_start__lte=now,
        banner_date_stop__gte=now
    ).order_by('banner_date_start')  # Сортируем по дате начала показа
    return active_banners  # Возвращаем список активных баннеров

def rotate_banners():
    """
    Выполнить ротацию баннеров, скрывая те, которые больше не должны отображаться.
    """
    now = timezone.now()  # Получаем текущее время
    # Находим все баннеры, которые видимы и у которых дата окончания показа меньше текущего времени
    banners_to_hide = Banner.objects.filter(banner_visible=True, banner_date_stop__lt=now)

    for banner in banners_to_hide:
        banner.banner_visible = False  # Устанавливаем статус видимости в False
        banner.save()  # Сохраняем изменения в базе данных

def update_banner_views(banner_id):
    """
    Обновить количество просмотров баннера при его отображении.
    """
    try:
        banner = Banner.objects.get(banner_id=banner_id)  # Находим баннер по его уникальному идентификатору
        banner.view += 1  # Увеличиваем количество просмотров на 1 (замените views на view, если это имя поля)
        banner.save()  # Сохраняем изменения в базе данных
    except Banner.DoesNotExist:
        pass  # Если баннер не найден, просто пропускаем

def refresh_banners():
    """
    Обновить активные баннеры и скрыть устаревшие.
    """
    rotate_banners()  # Сначала выполняем ротацию баннеров
    return get_active_banners()  # Затем получаем список активных баннеров




def rotate_banners2():
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
    current_index = cache.get('current_banner_index', 0)

    if active_banners.exists():
        # Получаем баннер по индексу
        banner = active_banners[current_index]
        
        # Обновляем индекс для следующего запроса
        next_index = (current_index + 1) % active_banners.count()  # Циклический переход
        cache.set('current_banner_index', next_index, None)  # Обновляем индекс в кэше
        
        return banner  # Возвращаем текущий баннер
    return None  # Если активных баннеров нет, возвращаем None









# from datetime import datetime
# from .models import Banner

# class BannerService:
#     @staticmethod
#     def get_active_banners():
#         """Получить все активные баннеры, которые видимы и находятся в периоде показа."""
#         now = datetime.now()
#         return Banner.objects.filter(
#             banner_visible=True,
#             banner_date_start__lte=now,
#             banner_date_stop__gte=now
#         ).order_by('banner_date_start')

#     @staticmethod
#     def rotate_banners():
#         """Проводит ротацию баннеров, выбирая следующий активный баннер."""
#         active_banners = BannerService.get_active_banners()
#         if active_banners.exists():
#             # Получаем первый баннер в списке активных
#             current_banner = active_banners.first()
#             # Увеличиваем количество просмотров
#             current_banner.views += 1
#             current_banner.save()
#             return current_banner
#         return None

#     @staticmethod
#     def update_banner(banner_id, data):
#         """Обновить информацию о баннере."""
#         try:
#             banner = Banner.objects.get(banner_id=banner_id)
#             for attr, value in data.items():
#                 setattr(banner, attr, value)
#             banner.save()
#             return banner
#         except Banner.DoesNotExist:
#             return None
