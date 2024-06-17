#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document based on the name
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
