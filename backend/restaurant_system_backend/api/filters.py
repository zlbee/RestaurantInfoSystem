import django_filters
from .models import Restaurant

class RestaurantFilter(django_filters.FilterSet):
    """Restaurant filterset.

    Args:
        django_filters (django_filters.FilterSet): Basic filterset.
    """
    # filters
    # - location filter: contains, case insensitive
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    # - cuisine filter: contains, case insensitive
    cuisine = django_filters.CharFilter(field_name='cuisine', lookup_expr='icontains')

    # model config
    class Meta:
        # related model
        model = Restaurant
        # related fields
        fields = ['location', 'cuisine']
