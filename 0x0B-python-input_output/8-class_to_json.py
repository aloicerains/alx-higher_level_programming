#!/usr/bin/python3
"""Module class to Json"""

import json


def class_to_json(obj):
    """Function returns dictionary description of object"""

    return obj.__dict__
