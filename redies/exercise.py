from functools import wraps
import uuid
from typing import Callable, Union
import redis


redis_client = redis.Redis(host='localhost', port=6379)


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a particular function."""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def inner(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

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
