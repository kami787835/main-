from rest_framework import generics, viewsets
from .models import CallArticle, CallArticleImage
from .serializers import CallArticleSerializer, CallArticleImageSerializer

# Создание статьи
class CallArticleCreateAPIView(generics.CreateAPIView):
    queryset = CallArticle.objects.all()
    serializer_class = CallArticleSerializer

# Получение списка статей
class CallArticleListAPIView(generics.ListAPIView):
    serializer_class = CallArticleSerializer

    def get_queryset(self):
        queryset = CallArticle.objects.all().order_by('-publication_date')
        lang = self.kwargs.get("lang")  # Если lang отсутствует, будет None
        return self.filter_by_language(queryset, lang)

    def filter_by_language(self, queryset, lang):
        if lang and hasattr(queryset.model, 'language'):
            return queryset.filter(language=lang)
        return queryset
