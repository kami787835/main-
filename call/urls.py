from django.urls import path
from .views import CallArticleCreateAPIView, CallArticleListAPIView

urlpatterns = [
    path('articles/create/', CallArticleCreateAPIView.as_view(), name='call--create'),
    path('articles/<str:lang>/', CallArticleListAPIView.as_view(), name='call--list-by-lang'),
]
