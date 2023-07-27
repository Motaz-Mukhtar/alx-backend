#!/usr/bin/env python3
"""
    MRUCache Class.
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
        Assign MRUCache Class.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            Assign to the dict self.cache_data
            the item value for the key 'key'
            if key or item is None, this method
            should not do anything, if the
            number of items in self.cache_data
            is higher than BaseCaching.MAX_ITEMS,
            Discard the most recently used item
            (MRU Algorithm).
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

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
