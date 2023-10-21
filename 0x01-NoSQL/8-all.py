#!/usr/bin/env python3
"""
list all documents in mongo db
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
