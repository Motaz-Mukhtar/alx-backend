#!/usr/bin/env python3
"""
    Create function index_range()
"""
from typing import Tuple


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
