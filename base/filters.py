import django_filters
from .models import Blog


class BlogPostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = Blog
        fields = ['category']