#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in
                                      range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Union[int, List[List[str]]]]:
        """Return a dictionary with pagination information"""
        if index is None:
            raise TypeError("Index cannot be None")
        assert 0 <= index < len(self.indexed_dataset())

        data: List[List[str]] = []
        indexC = index
        while len(data) < page_size and indexC < len(self.indexed_dataset()):
            if indexC in self.indexed_dataset():
                data.append(self.indexed_dataset()[indexC])
            indexC += 1

        return {
            "index": index,
            "next_index": indexC,
            "page_size": len(data),
            "data": data,
        }
