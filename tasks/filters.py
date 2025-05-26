from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    assigned_to = filters.NumberFilter(field_name="assigned_to__id")
    completed = filters.BooleanFilter(field_name="completed")
    created_at = filters.DateFromToRangeFilter()
    points = filters.RangeFilter()