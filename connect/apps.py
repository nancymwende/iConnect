from django.apps import AppConfig


class ConnectConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "connect"

    def ready(self):
        # trunk-ignore(flake8/F401)
        import connect.signals


default_app_config = "connect.apps.ConnectConfig"
