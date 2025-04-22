from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

class NewsListView(generics.ListCreateAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all().order_by('-publication_date')
        lang = self.kwargs.get("lang", None)
        if lang:
            queryset = self.filter_by_language(queryset, lang)
        return queryset

    def filter_by_language(self, queryset, lang):
        if lang and hasattr(queryset.model, 'language'):
            return queryset.filter(language=lang)
        return queryset
