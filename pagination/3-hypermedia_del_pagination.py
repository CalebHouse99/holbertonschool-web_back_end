#!/usr/bin/env python3
"""What in documentation?"""
import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None
        self.__dataset = self.dataset()
        self.__indexed_dataset = self.indexed_dataset()

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination data resilient to deletion"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = list(self.__indexed_dataset.items())\
        [index:index + page_size]
        page_data = [item[1] for item in indexed_data]
        next_index = max(indexed_data)[0] + 1 if indexed_data else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }


def index_range(page, page_size):
    """Tuple of size two with start and end"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)