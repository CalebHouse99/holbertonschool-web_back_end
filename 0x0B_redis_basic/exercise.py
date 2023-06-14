#!/usr/bin/env python3
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self.redis.flushdb()
    
    def store(data) -> str:
        randKey = uuid.uuid4()
        