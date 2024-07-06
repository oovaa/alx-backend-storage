#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange(
    "{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange(
    "{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format([i.decode('utf-8') for i in inputs]))
print("outputs: {}".format([o.decode('utf-8') for o in outputs]))
