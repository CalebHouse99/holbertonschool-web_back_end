#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        randKey = uuid.uuid4()
        self._redis.set(str(randKey), data)
        return str(randKey)

    def get(self, key: str, fn: Callable = None):
        if key is None:
            return None
        val = self._redis.get(key)
        if val is None:
            return None
        if fn:
            return fn(val)
        else:
            return val

    def get_str(self, key):
        return self.get(key, str)

    def get_int(self, key):
        return self.get(key, int)
