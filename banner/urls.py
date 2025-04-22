from django.urls import path
from .views import ActiveBannersView, BannerView, BannerView2,BannerView3

urlpatterns = [
    path('api0/banners/', ActiveBannersView.as_view(), name='active-banners'),  # Эндпоинт для активных баннеров
    path('api1/banners/', BannerView.as_view(), name='banner-list'),
    path('api2/banners/', BannerView2.as_view(), name='banner-list'),
    path('api/banners/', BannerView3.as_view(), name='banner-list'),
]

#  path('api2/banners/', BannerView2.as_view(), name='banner-list'),







# from django.urls import path
# from .views import BannerListView

# urlpatterns = [
#     path('api/banners/', BannerListView.as_view(), name='banner-list'),  # Маршрут для получения списка активных баннеров
# ]
