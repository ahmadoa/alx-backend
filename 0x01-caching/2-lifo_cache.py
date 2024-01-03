#!/usr/bin/env python3
"""2. LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """caching system using LIFO"""

    def __init__(self):
        """initialize LIFOCache"""
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
            else:
                self.__tracking.append(self.__tracking.pop(
                    self.__tracking.index(key)
                ))
            return

        if key not in self.__tracking:
            popped_key = self.__tracking.pop()
            self.cache_data.pop(popped_key)
            print('DISCARD: {}'.format(popped_key))
            self.__tracking.append(key)
        return

    def get(self, key):
        """returns value for matching key in cache"""
        return self.cache_data.get(key, None)
