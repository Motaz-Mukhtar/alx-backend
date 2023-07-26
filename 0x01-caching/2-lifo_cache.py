#!/usr/bin/env python3
"""
    LIFOCache Class.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        Assign LIFOCache Class.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Assign to the dict self.cache_data
            the item value for the key 'key',
            if key or item is None, this method
            should not do anyhing, if the number
            of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, you must
            Discard the last put in cache.
        """
        if key is None or item is None:
            return None
        if len(self.cache_data) >= 1:
            last_item = list(self.cache_data)[-1]
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(last_item))
            del self.cache_data[last_item]

    def get(self, key):
        """
            Return the value in self.cache_data
            linked to key, if key is None or if
            the key doesn't exist in self.cache_data
            return None.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
