from django.urls import path
from .views import NewsListView

urlpatterns = [
    path('news/<str:lang>/', NewsListView.as_view(), name='main_news_read'),
]
