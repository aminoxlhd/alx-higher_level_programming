#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    ave = 0
    div = 0
    for list in my_list:
        ave += list[0] * list[1]
        div += list[1]
    return float(ave / div)
