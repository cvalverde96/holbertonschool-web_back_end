#!/usr/bin/env python3

"""
a Python function that lists all documents in a collection
Return an empty list if no document in the collection
"""
from pymongo.collection import Collection
from typing import List, Dict, Any, Optional


def list_all(mongo_collection: Optional[Collection]) -> List[Dict[str, Any]]:
    """_summary_

    Args:
        mongo_collection (Optional[Collection]): a collection object

    Returns:
        List[Dict[str, Any]]: a list of dictionaries
    """
    return [] if mongo_collection is None else list(mongo_collection.find())
