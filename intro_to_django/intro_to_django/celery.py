import os
from celery import Celery

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "intro_to_django.settings"
)
app = Celery("intro_to_django")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()