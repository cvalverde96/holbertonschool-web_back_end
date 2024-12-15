#!/usr/bin/env python3

"""
 a Python function that inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """_summary_

    Args:
        mongo_collection (_type_): a collection object

    Returns:
        _type_: a new document ID
    """
    new_doc = mongo_collection.insert_one({**kwargs})
    return new_doc.inserted_id
