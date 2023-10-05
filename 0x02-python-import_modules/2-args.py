#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    count = len(sys.argv) - 1

    print("{} arguments{}{}".format(
        count, "s" if count != 1 else "", ":" if count else "."))

    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
