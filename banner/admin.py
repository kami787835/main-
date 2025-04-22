from django.contrib import admin
from .models import Banner, File

class FileInline(admin.TabularInline):
    """Inline для отображения связанных файлов в админке баннеров."""
    model = Banner.files.through  # Модель связи ManyToMany
    extra = 1  # Количество пустых форм для добавления новых файлов

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    """Админский интерфейс для модели Banner."""
    list_display = ('banner_id', 'banner_title', 'banner_visible', 'banner_date_start', 'banner_date_stop', 'views')
    list_filter = ('banner_visible', 'banner_date_start', 'banner_date_stop')
    search_fields = ('banner_id', 'banner_title', 'banner_key')
    ordering = ('banner_date_start',)
    inlines = [FileInline]  # Отображаем связанные файлы в админке

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """Админский интерфейс для модели File."""
    list_display = ('file_id', 'file_name', 'file_ext', 'file_date')
    search_fields = ('file_id', 'file_name')
    ordering = ('file_date',)
