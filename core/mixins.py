from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest
from typing import cast


class SuperuserPermissionRequiredMixin(PermissionRequiredMixin):
    request: HttpRequest

    def has_permission(self) -> bool:
        user = cast(User, self.request.user)
        if user.is_authenticated and user.is_superuser:
            return True
        return super().has_permission()
