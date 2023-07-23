#!/usr/bin/env python3
"""
    Create Server Class
"""

import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Returns a dictionary containing the following
            key-value pairs:
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page
                      (equivalent to return from previous task)
                next_page: number of the next page, None if no next page
                prev_page: number of the previous page,
                           None if no previous page
                total_pages: the total number of pages in
                             the dataset as an integer
        """
        data = self.get_page(page, page_size)
        if self.get_page(page + 1, page_size) == []:
            next_page = None
        else:
            next_page = page + 1
        if page <= 1:
            prev_page = None
        elif self.get_page(page - 1, page_size) == []:
            prev_page = None
        else:
            prev_page = page - 1
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {"page_size": page_size, "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": total_pages}


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
