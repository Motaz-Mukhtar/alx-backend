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
            Assign to the dict self.cache_data
            the item value for the key 'key',
            if key or item is None, this method
            should ot do anything, if the number
            of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, then you
            must discard the first item in cache.
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data)[0]))
            del self.cache_data[list(self.cache_data)[0]]

    def get(self, key, item):
        """
            Return the value in self.cache_data
            linked to key, if key is None or if
            the key doesn't exists in
            self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
