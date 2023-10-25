#!/usr/bin/env python3

"""import a module"""

from base_caching import BaseCaching

"""create a class"""


class LRUCache(BaseCaching):
    """class that inherits from BaseCaching"""

    def __init__(self):
        """call the parent init"""
        super().__init__()
        self.order_keys = []

    def put(self, key, item):
        """functions that inserts items into the cache with FIFO strategy"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= \
                self.MAX_ITEMS and key not in self.cache_data:
            discarded_key = self.order_keys.pop(0)
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
