from django.contrib import admin
from .models import News, NewsImage

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'category', 'views', 'publication_date')
    list_filter = ('language', 'category', 'publication_date')
    search_fields = ('title', 'content', 'category')
    inlines = [NewsImageInline]

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

admin.site.register(News, NewsAdmin)
