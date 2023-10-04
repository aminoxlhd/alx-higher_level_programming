#!/usr/bin/python3
letter = 0
for letter1 in range(ord("z"), ord("a") -1 , -1):
    print("{}".format(chr(letter1 - letter)), end="")
    letter = 32 if letter == 0 else 0
