from django.urls import path
from .views import NewsArticleCreateAPIView, NewsArticleListAPIView, NewsArticleDetailView

urlpatterns = [
    path('create/', NewsArticleCreateAPIView.as_view(), name='news-create'),
    path('<str:lang>/', NewsArticleListAPIView.as_view(), name='news-list'),
    path('detail/<int:pk>/', NewsArticleDetailView.as_view(), name='news-detail'),
]
