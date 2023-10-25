#!/usr/bin/env python3

"""import a module"""

from base_caching import BaseCaching

"""create a class"""


class MRUCache(BaseCaching):
    """class that inherits from BaseCaching"""

    def __init__(self):
        """call the parent init"""
        super().__init__()
        self.order_keys = []

    def put(self, key, item):
        """functions that inserts items into the cache with MRU strategy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order_keys.remove(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.order_keys.pop()
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        if key not in self.cache_data:
            self.order_keys.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """function that returns value linked to key"""

        if key is None:
            return None

        if key in self.cache_data:
            self.order_keys.append(key)
            return self.cache_data[key]
        return None
