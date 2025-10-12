from rest_framework import permissions
from .permissions import Ishandlingeditorpermission


class handlingeditorPermissonMixin():
    Permission_classes = [permissions.IsAdminUser, Ishandlingeditorpermission]