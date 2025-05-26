from rest_framework import permissions

class IsGuardian(permissions.BasePermission):
    """
    Permite acesso apenas a usuários do tipo 'guardian'.
    """
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'guardian'
