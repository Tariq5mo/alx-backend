#!/usr/bin/python3
"""
	"""
from base_caching import BaseCaching



class BasicCache(BaseCaching):
    """

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """
        """
        super().cache_data

    def put(self, key, item) -> None:
        self.cache_data[key] = item

    def get(self, key):
        return super().get(key)
