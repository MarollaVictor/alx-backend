#!/usr/bin/env python3
"""A module for a basic caching system without size limit."""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """A basic caching system allowing unlimited storage."""

    def put(self, key, item):
        """Add an item to the cache.
        Args:
            key (any): Key to store the item.
            item (any): Item to be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item  # Directly assign to dictionary

    def get(self, key):
        """Retrieve an item from the cache by key.
        Args:
            key (any): Key to look up.
        Returns:
            any: Value associated with key, or None if key doesn't exist.
        """
        return self.cache_data.get(key) if key is not None else None
