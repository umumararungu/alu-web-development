#!/usr/bin/python3
""" 0. Basic dictionary
"""
import *

class BaseCaching:
    'print(__import__("my_module").MyClass.__doc__)'
    def __init__(self):
        'print(__import__("my_module").my_function.__doc__)'
        self.cache_data = {}

class BasicCache(BaseCaching):
    'print(__import__("my_module").MyClass.__doc__)'
    def put(self, key, item):
        'print(__import__("my_module").my_function.__doc__)'
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        'print(__import__("my_module").my_function.__doc__)'
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    