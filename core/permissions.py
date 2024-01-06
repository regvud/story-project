from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsPremium(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.account and request.user.account.is_premium)


class IsWriter(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.account and request.user.account.is_writer)
