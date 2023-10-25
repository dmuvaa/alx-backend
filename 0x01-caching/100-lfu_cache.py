#!/usr/bin/env python3

"""import some models"""

from base_caching import BaseCaching

"""create a class"""


class LFUCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching via LFU"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for the key key"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_used_key = min(self.keys, key=lambda k: (self.uses[k], self.keys.index(k)))
                self.cache_data.pop(least_used_key)
                self.keys.remove(least_used_key)
                self.uses.pop(least_used_key)
                print("DISCARD:", least_used_key)
        
        else:
            self.keys.remove(key)
        
        self.cache_data[key] = item
        self.keys.append(key)
        self.uses[key] = self.uses.get(key, 0) + 1

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None:
            return None
        if key in self.cache_data:
            self.uses[key] += 1
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
