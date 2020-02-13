from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = "navoica_enroll.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import navoica_enroll.users.signals  # noqa F401
        except ImportError:
            pass
