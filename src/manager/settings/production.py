import os
from .base import BASE_DIR, DATABASES

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['freelancemanager.herokuapp.com']

# database
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Celery settings
from celery.schedules import crontab
BROKER_POOL_LIMIT = 3
CELERY_BROKER_URL = 'amqp://sjyqatxw:3WTXHzqGWgctcNNEbFCki21X-3FXt91_@stingray.rmq.cloudamqp.com/sjyqatxw'
CELERY_TIMEZONE = 'Europe/London'
CELERY_BEAT_SCHEDULE = {
    'populate-db': {
        'task': 'dashboard.tasks.repopulate_db',
        'schedule': crontab(hour=[7, 13, 17], minute=[0, 0, 0],  day_of_week='*'),
    },
}
