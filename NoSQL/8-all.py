#!/usr/bin/env python3

"""
a Python function that lists all documents in a collection
"""

from pymongo.collection import Collection
from typing import Dict, Any, Optional, Iterable


def list_all(mongo_collection: Optional[Collection]) -> Iterable[Dict[str, Any]]:
    """_summary_

    Args:
        mongo_collection (Optional[Collection]): instance of pymongo collection

    Returns:
        Iterable[Dict[str, Any]]: list of documents in collection
    """
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find()
