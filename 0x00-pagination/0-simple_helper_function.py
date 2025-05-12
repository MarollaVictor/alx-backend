#!/usr/bin/env python3
import csv
import requests
from typing import List, Dict, Tuple

class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_URL = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv"
    
    def __init__(self):
        self.__dataset = None
    
    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            response = requests.get(self.DATA_URL)
            response.encoding = 'utf-8'
            self.__dataset = list(csv.reader(response.text.splitlines()))
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset.
        
        Args:
            page: Page number (1-indexed)
            page_size: Number of items per page
            
        Returns:
            List of rows for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        
        if start >= len(dataset):
            return []
        
        return dataset[start:end]

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end index for pagination.
    
    Args:
        page: Current page number (1-indexed)
        page_size: Number of items per page
        
    Returns:
        Tuple of (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)