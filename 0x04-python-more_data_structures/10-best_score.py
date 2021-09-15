#!/usr/bin/python3
def best_score(a_dictionary):
    """Function returns a key with beggest integer value:"""
    if a_dictionary is not None:
        keys = list(a_dictionary.keys())
        a = int(a_dictionary[keys[0]])
        flag = 1
        for i, j in a_dictionary.items():
            if j > a:
                a = int(j)
            elif a == int(j):
                flag = flag * 1
                continue
            flag = flag * 0
        if flag == 1:
            return None
        else:
            return a
