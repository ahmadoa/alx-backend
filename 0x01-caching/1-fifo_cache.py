#!/usr/bin/env python3
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """caching system using FIFO"""

    def __init__(self):
        """initialize FIFOCache"""
        super().__init__()
        self.__tracking = []

    def put(self, key, item):
        """inserts new key value pair into cache"""
        if not all([key, item]):
            return
        self.cache_data.update({key: item})

        if len(self.cache_data) <= self.MAX_ITEMS:
            if key not in self.__tracking:
                self.__tracking.append(key)
            return

        if key not in self.__tracking:
            popped_key = self.__tracking.pop(0)
            self.cache_data.pop(popped_key)
            print('DISCARD: {}'.format(popped_key))
            self.__tracking.append(key)
        return

    def get(self, key):
        """returns value for matching key in cache"""
        return self.cache_data.get(key, None)
