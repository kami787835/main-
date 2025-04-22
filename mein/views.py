from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import NewsArticle
from .serializers import NewsArticleSerializer

class NewsArticleCreateAPIView(generics.CreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class NewsArticleListAPIView(generics.ListAPIView):
    serializer_class = NewsArticleSerializer

    def get_queryset(self):
        queryset = NewsArticle.objects.all().order_by('-publication_date')
        lang = self.kwargs.get("lang", None)
        return self.filter_by_language(queryset, lang)

    def filter_by_language(self, queryset, lang):
        if lang and hasattr(queryset.model, 'language'):
            return queryset.filter(language=lang)
        return queryset

class NewsArticleDetailView(generics.RetrieveAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
