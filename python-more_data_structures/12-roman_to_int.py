#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    integer_value = 0
    previous_value = 0

    for numeral in reversed(roman_string):
        current_value = roman_to_int_mapping[numeral]

        if current_value >= previous_value:
            integer_value += current_value
        else:
            integer_value -= current_value

        previous_value = current_value

    return integer_value