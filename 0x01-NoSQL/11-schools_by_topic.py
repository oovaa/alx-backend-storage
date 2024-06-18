#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def schools_by_topic(mongo_collection, topic):
    """
    a Python function that returns the list of school having a specific topic:
    """
    return mongo_collection.find({topic: topic})
