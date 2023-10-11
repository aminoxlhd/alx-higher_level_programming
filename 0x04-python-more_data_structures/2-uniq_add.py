#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    new_list2 = 0
    for i in new_list:
        new_list2 += i
    return new_list2
