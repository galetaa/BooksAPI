from ...utils import retry
from celery import shared_task


@shared_task
@retry(times=5, delay=2, exceptions=(ConnectionError,))
def send_book_message(action, book_id):
    print(f"Sending message: {action} for book {book_id}")
