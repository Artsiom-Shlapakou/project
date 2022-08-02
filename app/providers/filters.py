from crypt import methods
from django_filters import rest_framework as filters
from providers.models import Provider


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class ProviderFilterSet(filters.FilterSet):
    product = NumberInFilter(field_name='product', method='filter_by_product')
    country = filters.CharFilter(field_name='country', method='filter_by_country')

    def filter_by_country(self, queryset, name, value):
        return queryset.filter(contacts__address__country=value)
    
    def filter_by_product(self, queryset, name, value):
        return queryset.filter(products__id__in=value)

    class Meta:
        model = Provider
        fields = ['country', 'product']
