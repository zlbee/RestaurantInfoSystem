from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Api app configs.

    Args:
        AppConfig (AppConfig): Basic app config.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
