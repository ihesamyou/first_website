import os
from celery import Celery

# from django.db.utils import DEFAULT_DB_ALIAS, load_backend

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings")

app = Celery("personal_website", broker=os.environ.get("CELERY_BROKER_URL"))

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# def create_connection(alias=DEFAULT_DB_ALIAS):
#     connections.ensure_defaults(alias)
#     connections.prepare_test_settings(alias)
#     db = connections.databases[alias]
#     backend = load_backend(db["ENGINE"])
#     return backend.DatabaseWrapper(db, alias)
