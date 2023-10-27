#!/usr/bin/env python3

"""Import a few Modules"""

import csv
import math
from typing import List


"""create a funtion"""


def index_range(page, page_size):
    """function should return a tuple of size two"""
    index1 = (page - 1) * page_size
    index2 = page * page_size
    return (index1, index2)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initialize the dataset"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function that takes 2 arguments"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index1, index2 = index_range(page, page_size)
        return self.dataset()[index1:index2]
