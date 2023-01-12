#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) == str:
        return 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    intg = 0
    if roman_string[0] in roman:
        digit = roman[(roman_string[0])]
        for i in range(len(roman_string)):
            if roman_string[i] in roman:
                if roman[(roman_string[i])] > digit:
                    intg += (roman[(roman_string[i])] - digit) - digit
                else:
                    intg += roman[(roman_string[i])]
                    digit = roman[(roman_string[i])]
            else:
                return 0
        return intg
    return 0
