from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.assign_by == request.user