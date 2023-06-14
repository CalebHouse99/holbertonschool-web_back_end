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
