#!/usr/bin/python3
""" Defines function """
import json


def load_from_json_file(filename):
    """ creates an Object """
    with open(filename) as f:
        return json.load(f)
