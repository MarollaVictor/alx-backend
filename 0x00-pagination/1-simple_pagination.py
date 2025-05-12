import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.
    
    Args:
        page: Current page number (1-indexed)
        page_size: Number of items per page
        
    Returns:
        Tuple of (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset.
        
        Args:
            page: Page number (1-indexed, default 1)
            page_size: Number of items per page (default 10)
            
        Returns:
            List of rows for the requested page
            Empty list if arguments are out of range
        """
        # Verify arguments are positive integers
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"
        
        # Get the pagination range
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        
        # Return empty list if range is invalid
        if start >= len(dataset):
            return []
        
        return dataset[start:end]