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

        # Check if the item is already in the cache
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update the order of keys since it's recently used
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                old_key = self.order.pop()
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """3. LRU CachingCaching
        """
        if key is None or key not in self.cache_data:
            return None
        
                # Move the accessed key to the end to show that it was recently used
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]
