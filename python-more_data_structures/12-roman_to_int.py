#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    prev = 0
    if roman_string is None or not isinstance(roman_string, str):
        return result
    roman_string = roman_string.upper()
    for symbol in reversed(roman_string):
        value = roman_num[symbol]
        if value >= prev:
            result += value
        else:
            result -= value
        prev = value
    return result
