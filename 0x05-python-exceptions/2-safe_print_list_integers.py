#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    star = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            star += 1
    print()
    return star
