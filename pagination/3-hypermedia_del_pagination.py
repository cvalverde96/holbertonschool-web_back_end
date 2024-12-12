#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """_summary_

        Args:
            index (int, optional): starting index. Defaults to None.
            page_size (int, optional): size of the page. Defaults to 10.

        Returns:
            Dict: returns dictionary with index, next_index, page_size and data
        """
        if index is None:
            index = 0

        dataset = self.indexed_dataset()

        assert index >= 0 and index < len(dataset)

        data = []
        curr_index = index
        items_count = 0

        while items_count < page_size and curr_index < len(dataset):
            if curr_index in dataset:
                data.append(dataset[curr_index])
                items_count += 1
            curr_index += 1

        next_index = curr_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }