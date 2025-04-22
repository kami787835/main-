from django.contrib import admin
from .models import NewsArticle, NewsArticleImage


class NewsArticleImageInline(admin.TabularInline):
    model = NewsArticleImage
    extra = 1  # Количество пустых форм, отображаемых по умолчанию

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'publication_date','language')
    search_fields = ('title', 'content', 'category','language')
    list_filter = ('language',)
    inlines = [NewsArticleImageInline]

    def has_change_permission(self, request, obj=None):
        # Разрешаем изменение только суперпользователям
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Разрешаем удаление только суперпользователям
        return request.user.is_superuser

    def has_add_permission(self, request):
        # Разрешаем добавление только суперпользователям
        return request.user.is_superuser

admin.site.register(NewsArticle, NewsArticleAdmin)
