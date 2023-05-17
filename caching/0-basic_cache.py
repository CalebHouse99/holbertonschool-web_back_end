#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from BaseCaching.
    This caching system doesnt have a limit.
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesnt exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
