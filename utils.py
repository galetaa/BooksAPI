import time
from functools import wraps


def retry(times=3, delay=1, exceptions=(Exception,)):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            attempts = 0
            while attempts < times:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= times:
                        raise e
                    print(f"Retrying {func.__name__} due to {str(e)}, attempt {attempts}...")
                    time.sleep(delay)

        return wrapper_retry

    return decorator_retry
