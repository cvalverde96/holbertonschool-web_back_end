#!/usr/bin/env python3

"""
a Python function that changes all topics of a school
document based on the name
"""

from pymongo.collection import Collection
from typing import List


import pymongo
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """_summary_

    Args:
        mongo_collection (_type_): a collection object
        name (str): a string
        topics (List[str]): a list of strings

    Returns:
        _type_: an instance of pymongo.results.UpdateResult
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
