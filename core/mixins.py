from django.contrib.auth.mixins import PermissionRequiredMixin


class SuperuserPermissionRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        if self.request.user.is_superuser: # noqa
            return True
        return super().has_permission()
