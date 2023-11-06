#!/usr/bin/python3
""" Defines function """


def inherits_from(obj, a_class):
    """ Check if an object is exactly an instance of a given class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
