from rest_framework import permissions
from .permissions import IsStaffEditorPermissions


class StaffEditorPermissionsMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermissions
        ]