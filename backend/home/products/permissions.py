from rest_framework import permissions

class Ishandlingeditorpermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if request.user.is_staff:
            return True
        print(user.get_all_permissions())
        return False
    
