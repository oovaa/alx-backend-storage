from functools import wraps
import uuid
from typing import Callable, Union
import redis


redis_client = redis.Redis(host='localhost', port=6379)


def call_history(func):

    @wraps(func)
    def inner(self, *a, **k):
        fun_name = func.__qualname__

        in_key = fun_name + ":inputs"
        out_key = fun_name + ":outputs"

        self._redis.rpush(in_key, *a, **k)
        data = func(self, *a, **k)
        self._redis.rpush(out_key, data)

    return inner


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    @wraps(method)
    def inner(self, *args, **kwargs):
        redis_client.incr(method.__qualname__)

        return method(self, *args, **kwargs)
    return inner


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Callable = None):
        val = self._redis.get(key)
        return fn(val) if fn else val

    def get_int(self, key: str):
        return int(self._redis.get(key))

    def get_str(self, key: str):
        return str(self._redis.get(key))
