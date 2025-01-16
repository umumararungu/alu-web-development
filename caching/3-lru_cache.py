#!/usr/bin/python3
""" 3. LRU Caching
"""

from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ 3. LRU CachingCaching
    """
    def __init__(self):
        """3. LRU CachingCaching
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ 3. LRU CachingCaching
        """
        if key is None or item is None:
            return


        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            old_key = self.order.pop(0)
            del self.cache_data[old_key]
            print(f"DISCARD: {old_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """3. LRU CachingCaching
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
