#!/usr/bin/env python3
"""New class FICOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching system"""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Classic caching, we need a put"""
        if key is None or item is None:
            return None
        if len(self.keys) == BaseCaching.MAX_ITEMS and \
                key not in self.cache_data:
            discarded_key = self.keys.pop(0)
            del self.cache_data[discarded_key]
            print('DISCARD:', discarded_key)
        elif key not in self.cache_data:
            self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """We also need a get for caching"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
