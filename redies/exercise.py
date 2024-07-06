import functools
import uuid
from typing import Callable, Union
import redis


# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379)


def count_calls(method):
    @functools.wraps(method)
    def inner(self, *args, **kwargs):
        redis_client.incr(method.__qualname__)

        return method(self, *args, **kwargs)
    return inner


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
