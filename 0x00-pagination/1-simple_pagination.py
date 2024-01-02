#!/usr/bin/env python3
"""1. simple pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """class to paginate a db of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns appropriated paginated data based on inputs"""
        assert all([isinstance(page, int), isinstance(page_size, int)])
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index: end_index]
