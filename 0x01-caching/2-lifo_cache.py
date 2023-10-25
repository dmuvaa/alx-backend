#!/usr/bin/env python3

"""import a module"""

from base_caching import BaseCaching

"""create a class"""


class LIFOCache(BaseCaching):
    """caching system class that inherits from Basecaching"""
    def __init__(self):
        """Initialize a call parent class"""
        super().__init__()
        self.order_keys = []

    def put(self, key, item):
        """func that inserts items into cache with LIFO strategy"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= \
                self.MAX_ITEMS and key not in self.cache_data:
            discarded_key = self.order_keys.pop(-1)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        if key not in self.cache_data:
            self.order_keys.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """function that returns value linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
