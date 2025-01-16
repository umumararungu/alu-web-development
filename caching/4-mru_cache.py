#!/usr/bin/python3
""" 4. MRU Caching
"""

from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ 4. MRU CachingCaching
    """
    def __init__(self):
        """4. MRU CachingCaching
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ 4. MRU CachingCaching
        """
        if key is None or item is None:
            return

        # Check if the item is already in the cache
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update the order of keys since it's recently used
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                old_key = self.order.pop(-1)
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """4. MRU CachingCaching
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
