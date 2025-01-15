#!/usr/bin/python3
""" 1. FIFO caching
"""

# from collections import deque
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        # self.cache_data = {}

    def put(self, key, item):
        if key is None or item is None:
            return 

        if key in self.cache_data:
            self.cache_data[key] = item
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            old_key = self.order.popleft()
            del self.cache_data[old_key]
            print(f"DISCARD:{old_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self,key):
        if key is None or key not in len(self.cache_data):
            return None
        return self.cache_data[key]
