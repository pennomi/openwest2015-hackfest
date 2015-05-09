from rest_framework import permissions


class UserPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        

    def has_object_permission(self, request, view, obj):
        is_authed = super().has_object_permission(request, view, obj)
        print(request.user, obj)
        if request.user != obj:
            return False
        return is_authed