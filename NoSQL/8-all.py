#!/usr/env/ python3

"""
a Python function that lists all documents in a collection
"""

from pymongo.collection import Collection
from typing import List, Dict, Any


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """_summary_

    Args:
        mongo_collection (Collection): a pymongo collection object

    Returns:
        List[Dict[str, Any]]: a list of dictionaries
    """
    if mongo_collection == []:
        return []
    else:
        return list(mongo_collection.find({}))
