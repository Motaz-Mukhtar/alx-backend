#!/usr/bin/env python3
"""
    Create Server Class
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """
            Return appropirate page of the dataset.
        """
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)

        [start_index, end_index] = index_range(page, page_size)

        dataset = self.dataset()
        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple:
    """
        Return a tuple of size two containing a
        start index and an end index corresponding
        to the range of indexes.
    """
    if page == 1:
        start_index = 0
        end_index = page * page_size
        return (start_index, end_index)

    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
