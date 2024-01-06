from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

UserFunctionModel = get_user_model()


class UserFilter(filters.FilterSet):
    order = filters.OrderingFilter(
        fields=(
            "id",
            "email",
            "is_active",
            "is_block",
            "is_staff",
            "is_superuser",
        )
    )

    class Meta:
        model = UserFunctionModel
        fields = {
            "id": ("lt", "lte", "gt", "gte", "exact"),
            "email": ("startswith", "endswith", "icontains", "exact", "iexact"),
            "is_active": ("exact",),
            "is_block": ("exact",),
            "is_staff": ("exact",),
            "is_superuser": ("exact",),
        }
