from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task()
def repopulate_db():
    from dashboard.scripts.db_clean import clean_db
    from dashboard.scripts.db_populate import populate_db

    clean_db()
    populate_db()
    logger.info(">>> Database repopulated")


@shared_task()
def send_email_with_subscriptions_about_to_expire():
    # to be set
    from datetime import datetime
    my_time = datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")
    message = my_time + "Task not set yet."
    logger.info(message)
