from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

# Разрешение IsOwnerOrReadOnly проверяет, является ли пользователь владельцем этого объекта.
# Таким образом только при этом условии можно будет обновлять или удалять пост.
# Не-владельцы смогут получать пост, потому что это действие только для чтения.
