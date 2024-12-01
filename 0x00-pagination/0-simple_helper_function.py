#!/usr/bin/env python3
"""
This module contains a simple helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
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
