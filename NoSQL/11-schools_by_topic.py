#!/usr/bin/env python3

"""
a Python function that returns the list of school
having a specific topic
"""

import pymongo
from typing import List, Dict


def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """_summary_

    Args:
        mongo_collection (_type_): a pymongo collection object
        topic (str): a string representing the topic

    Returns:
        List[Dict]: a list of dictionaries containing the schools
    """
    return list(mongo_collection.find({"topics": topic}))
