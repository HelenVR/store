from celery import shared_task
from loguru import logger


@shared_task
def notify_product_change(product_name, action):
    logger.info(f"Product '{product_name}' has been {action}.")