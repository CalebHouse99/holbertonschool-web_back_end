#!/usr/bin/env python3
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        randKey = uuid.uuid4()
        self._redis.set(str(randKey), data)
        return str(randKey)

    def get(self, key: str, fn):
        if key is None:
            self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self):
        return str(self.get())

    def get_int(self):
        return int(self.get())
