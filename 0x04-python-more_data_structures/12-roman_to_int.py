#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman_string or type(roman_string) != str:
        return 0
    roman_2 = 0
    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            roman_2 += roman[roman_string[i]] - 2 * \
                    roman[roman_string[i - 1]]
        else:
            roman_2 += roman[roman_string[i]]
    return roman_2
