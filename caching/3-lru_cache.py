#!/usr/bin/env python3
"""New class LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching system"""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.keys) == BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            del self.cache_data[discarded_key]
            print('DISCARD:', discarded_key)
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
