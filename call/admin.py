from django.contrib import admin
from .models import CallArticle, CallArticleImage

class CallArticleImageInline(admin.TabularInline):
    model = CallArticleImage
    extra = 1

class CallArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'publication_date', 'language')
    list_filter = ('category', 'language', 'publication_date')
    search_fields = ('title', 'content', 'category')
    inlines = [CallArticleImageInline]

admin.site.register(CallArticle, CallArticleAdmin)
