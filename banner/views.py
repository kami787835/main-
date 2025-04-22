from rest_framework import generics, status
from rest_framework.response import Response
from .models import Banner
from .serializers import BannerSerializer  
from .services import get_active_banners, update_banner_views, refresh_banners
from rest_framework.views import APIView
from .services import get_active_banners, rotate_banners
from .services import get_next_banner, rotate_banners2



class ActiveBannersView(generics.ListAPIView):
    """
    Эндпоинт для получения активных баннеров.
    """
    serializer_class = BannerSerializer

    def get(self, request, *args, **kwargs):
        # Обновляем баннеры перед получением активных
        refresh_banners()  # Обновляем активные баннеры и скрываем устаревшие
        active_banners = get_active_banners()  # Получаем активные баннеры
        serializer = self.get_serializer(active_banners, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)  # Возвращаем данные в ответе





class BannerView(APIView):
    def get(self, request):
        rotate_banners()  # Выполняем ротацию баннеров
        active_banners = get_active_banners()  # Получаем случайные активные баннеры
        
        # Форматируем ответ
        banners_data = [
            {
                "banner_id": banner.banner_id,
                "banner_title": banner.banner_title,
                "banner_link": banner.banner_link,
                "banner_date": banner.banner_date,
                "views": banner.views,
                # Добавьте другие необходимые поля
            }
            for banner in active_banners
        ]

        return Response({"banners": banners_data})





class BannerView2(APIView):
    def get(self, request):
        rotate_banners2()  # Выполняем ротацию баннеров
        banner = get_next_banner()  # Получаем следующий активный баннер
        
        if banner:
            banner_data = {
                "banner_id": banner.banner_id,
                "banner_title": banner.banner_title,
                "banner_link": banner.banner_link,
                "banner_date": banner.banner_date,
                "views": banner.views,
                # Добавьте другие необходимые поля
            }
            return Response({"banner": banner_data})
        else:
            return Response({"message": "Нет доступных баннеров"}, status=404)




from .services2 import get_next_banner, refresh_banners

class BannerView3(APIView):
    """
    API для получения активных баннеров.
    """

    def get(self, request):
        """
        Обработчик GET-запроса для получения следующего активного баннера.
        """
        refresh_banners()  # Обновляем баннеры перед отправкой

        # Получаем следующий баннер
        banner = get_next_banner()

        if banner:
            # Если баннер найден, возвращаем его данные
            return Response({
                'banner_id': banner.banner_id,
                'banner_title': banner.banner_title,
                'banner_link': banner.banner_link,
                'banner_visible': banner.banner_visible,
                'views': banner.views,
            })
        else:
            # Если активных баннеров нет, возвращаем ошибку
            return Response({'error': 'Нет доступных баннеров'}, status=status.HTTP_404_NOT_FOUND)





# class BannerView2(APIView):



# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Banner
# from .serializers import BannerSerializer
# from .services import rotate_banners, refresh_banners, update_banner_views

# class BannerListView(generics.ListAPIView):
#     """
#     API View для получения списка активных баннеров.
#     """
#     serializer_class = BannerSerializer

#     def get(self, request, *args, **kwargs):
#         rotate_banners()  # Скрываем устаревшие баннеры
#         active_banners = refresh_banners()  # Обновляем активные баннеры
#         serializer = self.get_serializer(active_banners, many=True)

#         # Увеличиваем количество просмотров для каждого баннера
#         for banner in active_banners:
#             update_banner_views(banner.banner_id)

#         return Response(serializer.data)  # Возвращаем сериализованные данные

























# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Banner
# from .serializers import BannerSerializer
# from .services import BannerService

# class ActiveBannerListView(generics.ListAPIView):
#     """Представление для получения списка активных баннеров."""
#     serializer_class = BannerSerializer

#     def get_queryset(self):
#         """Получить все активные баннеры."""
#         return BannerService.get_active_banners()

# class BannerUpdateView(generics.UpdateAPIView):
#     """Представление для обновления баннера по его ID."""
#     serializer_class = BannerSerializer
#     lookup_field = 'banner_id'  # Используем banner_id в качестве уникального идентификатора

#     def get_queryset(self):
#         """Получить баннер по его ID."""
#         return Banner.objects.all()

#     def put(self, request, *args, **kwargs):
#         """Обновить баннер и вернуть его обновленные данные."""
#         banner_id = self.kwargs.get('banner_id')
#         data = request.data
#         updated_banner = BannerService.update_banner(banner_id, data)

#         if updated_banner:
#             serializer = self.get_serializer(updated_banner)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"detail": "Баннер не найден."}, status=status.HTTP_404_NOT_FOUND)

# class RotateBannerView(generics.GenericAPIView):
#     """Представление для ротации баннеров."""
    
#     def get(self, request, *args, **kwargs):
#         """Ротировать баннеры и вернуть текущий активный баннер."""
#         current_banner = BannerService.rotate_banners()

#         if current_banner:
#             serializer = BannerSerializer(current_banner)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"detail": "Нет доступных баннеров."}, status=status.HTTP_404_NOT_FOUND)
