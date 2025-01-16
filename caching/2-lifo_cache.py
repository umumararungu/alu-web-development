#!/usr/bin/python3
""" 2. LIFO Caching
"""

from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ 2. LIFO Caching
    """
    def __init__(self):
        """2. LIFO Caching
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ 2. LIFO Caching
        """
        if key is None or item is None:
            return

        # if key in self.cache_data:
        #     self.cache_data[key] = item
        #     return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            old_key = self.order.pop()
            del self.cache_data[old_key]
            print(f"DISCARD: {old_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """2. LIFO Caching
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
