#!/usr/bin/env python3
"""
	BasicCache Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
	"""
		Create BasicCache Class.
	"""
	def __inti__(self):
		super().__init__()

	def put(self, key, item):
		"""
		"""
		if key is None or item is None:
			return None
		self.cache_data[key] = item

	def get(self, key):
		"""
		"""
		if (key is None or
		    key not in self.cache_data):
			return None
		return self.cache_data[key]


my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

