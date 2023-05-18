#!/usr/bin/env python3
"""What in documentation?"""
import csv
import math
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__dataset = self.dataset()

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        if start >= len(self.__dataset) or end > len(self.__dataset):
            return []
        
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary of pagination data"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_pages
        }

def index_range(page, page_size):
    """Tuple of size two with start and end"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)