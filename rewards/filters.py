from django_filters import rest_framework as filters
from .models import Reward

class RewardFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    available = filters.BooleanFilter(field_name="available")
    created_at = filters.DateFromToRangeFilter()
    cost = filters.RangeFilter()