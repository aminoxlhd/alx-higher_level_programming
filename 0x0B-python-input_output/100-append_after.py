#!/usr/bin/python3
""" Defines function """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f2:
        f2.write(text)
