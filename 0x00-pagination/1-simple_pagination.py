#!/usr/bin/env python3
"""
This module contains a simple helper function for pagination.
"""
import csv
import math
from typing import List, Tuple
import unittest


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for
        the given pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)


class Server(unittest.TestCase):
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.
        """
        self.assertIsInstance(page, int)
        self.assertIsInstance(page_size, int)
        self.assertGreater(page, 0)
        self.assertGreater(page_size, 0)
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
