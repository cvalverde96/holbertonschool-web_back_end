#!/usr/bin/env python3

"""
 a Python function that inserts a new document in a collection based on kwargs
"""
from pymongo.collection import Collection
from typing import Any


def insert_school(mongo_collection: Collection, **kwargs: Any) -> Any:
    """_summary_

    Args:
        mongo_collection (Collection): a collection object

    Returns:
        Any: an id of the new document
    """
    new_doc = mongo_collection.insert_one({**kwargs})
    return new_doc.inserted_id
