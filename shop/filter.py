import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    manufacturer = django_filters.CharFilter(field_name='manufacturer__name', lookup_expr='icontains')
    size = django_filters.CharFilter(field_name='sizes__name', lookup_expr='icontains')
    color = django_filters.CharFilter(field_name='colors__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'manufacturer', 'size', 'color']
