#!/usr/bin/env python3
"""
    BasicCache Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        Assign BasicCache Class.
    """
    def put(self, key, item):
        """
            Assign to the directory
            self.cache_data the item
            value for the key.
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """
            Return the value in
            self.cache_data linked to
            key, if kye is None or if the key
            doesn't exists in self.cache_data
            return None.
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
