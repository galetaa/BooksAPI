# book_management/celery_app.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_management.settings')

app = Celery('book_management')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = 'amqp://localhost'  # Проверьте, что хост и порт указаны правильно
