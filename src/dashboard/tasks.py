from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime

logger = get_task_logger(__name__)
current_time = datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")


@shared_task()
def repopulate_db():
    from dashboard.scripts.db_clean import clean_db
    from dashboard.scripts.db_populate import populate_db

    clean_db()
    populate_db()

    message = current_time + "Database repopulated."
    logger.info(message)


@shared_task()
def send_mail_with_subscriptions_expired_and_about_to_expire():
    from subscriptions.scripts import send_mail_with_subscriptions_expired_and_about_to_expire as send
    send()
