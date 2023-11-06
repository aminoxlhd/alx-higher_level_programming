#!/usr/bin/python3
""" Defines a function """


def add_attribute(obj, att, value):
    """ add_attribute function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
