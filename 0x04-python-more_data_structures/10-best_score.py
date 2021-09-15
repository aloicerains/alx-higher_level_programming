#!/usr/bin/python3
def best_score(a_dictionary):
    """Function returns a key with beggest integer value:"""
    if a_dictionary is not None:
        keys = list(a_dictionary.keys())
        a = a_dictionary[keys[0]]
        for i, j in a_dictionary.items():
            if j > a:
                a = j
        return a
