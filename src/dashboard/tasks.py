from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task()
def repopulate_db():
    from dashboard.scripts.db_clean import clean_db
    from dashboard.scripts.db_populate import populate_db

    clean_db()
    logger.info(">>> Database cleaned")
    populate_db()
    logger.info(">>> Database populated")
