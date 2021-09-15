#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function converts roman to integer."""
    if str(roman_string):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L':
                  50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, k in enumerate(roman_string):
            if (i+1) == len(roman_string) or romans[k] >=\
              romans[roman_string[i + 1]]:
                result += romans[k]
            else:
                result -= romans[k]
        return result
    return 0
