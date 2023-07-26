#!/usr/bine/env python3
"""
    FIFOCache Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        Assign FIFOCache Class.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        """
    if key is None or item is None:
        return None

    if len(self.cache_data) > BaseCaching.MAX_ITEMS:
        
