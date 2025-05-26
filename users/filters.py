from django_filters import rest_framework as filters
from .models import User

class UserFilter(filters.FilterSet):
    username = filters.CharFilter(field_name="username", lookup_expr="icontains")
    email = filters.CharFilter(field_name="email", lookup_expr="icontains")
    user_type = filters.ChoiceFilter(field_name="user_type", choices=User.UserType.choices)
    date_joined = filters.DateFromToRangeFilter()