#!/usr/bin/env python3
"""A module implementing a FIFO-based caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that uses FIFO eviction policy when limits are exceeded."""

    def __init__(self):
        """Initialize the FIFO cache, extending the parent class."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache, evicting the oldest item if necessary.
        
        Args:
            key (any): The key under which the item is stored.
            item (any): The item to be stored in the cache.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the first item added
                evicted_key = self.order.pop(0)
                del self.cache_data[evicted_key]
                print(f"DISCARD: {evicted_key}")

    def get(self, key):
        """Retrieve an item from the cache by key.
        
        Args:
            key (any): The key for the item to retrieve.
            
        Returns:
            any: The item associated with the key, or None if not found.
        """
        return self.cache_data.get(key, None) if key is not None else None
