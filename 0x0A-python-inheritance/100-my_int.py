#!/usr/bin/python3
""" class MyInt """


class MyInt(int):
    """ function in Myint class """
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
