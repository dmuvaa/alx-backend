#!/usr/bin/env python3

"""Import a Module"""

import csv
import math
from typing import List


"""create a class"""


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize dataset"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index1, index2 = self.index_range(page, page_size)
        return self.dataset()[index1:index2]

    def index_range(self, page, page_size):
        """Function should return a tuple of size two"""
        index1 = (page - 1) * page_size
        index2 = page * page_size
        return (index1, index2)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with hypermedia pagination data."""
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        data = self.get_page(page, page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page - 1 > 0 else None

        hyper_dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper_dict
