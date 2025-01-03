#!/usr/bin/env python3
"""
This module contains a simple helper function for pagination.
"""
import csv
from typing import List, Tuple, Dict, Union
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
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Get a page from the dataset.

        Args:
            page (int, optional): The current page number. Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            List[List[str]]: The dataset page.
        """
        self.assertIsInstance(page, int)
        self.assertIsInstance(page_size, int)
        self.assertGreater(page, 0)
        self.assertGreater(page_size, 0)
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Union[List[List[str]], int, None]]:
        """
        Get a page from the dataset with hypermedia metadata.

        Args:
            page (int, optional): The current page number. Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            Dict[str, Union[List[List[str]], int, None]]:
                                    A dictionary containing:
                - page_size: The length of the returned dataset page.
                - page: The current page number.
                - data: The dataset page.
                - next_page: Number of the next page, None if no next page.
                - prev_page: Number of the previous page,
                                    None if no previous page.
                - total_pages: The total number of pages in the dataset.
        """
        try:
            dataset = self.get_page(page, page_size)
            di: Dict[str, Union[List[List[str]], int, None]] = {}
            total_items = len(self.dataset())
            total_pages = (total_items + page_size - 1) // page_size
            di["page_size"] = len(dataset)
            di["page"] = page
            di["data"] = dataset
            di["next_page"] = page + 1 if page < total_pages else None
            di["prev_page"] = page - 1 if page > 1 else None
            di["total_pages"] = total_pages
            return di
        except Exception:
            return {}
