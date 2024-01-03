#!/usr/bin/env python3
"""0. Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a caching system class"""

    def put(self, key, item):
        """inserts new key/value pair into cache"""
        if not all([key, item]):
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """returns value for matching key in cache"""
        return self.cache_data.get(key, None)
