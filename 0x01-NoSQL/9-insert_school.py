#!/usr/bin/env python3
"""
insert documents into mongo db
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
