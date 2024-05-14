#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # The items() method returns a view object that
    # displays a list of dictionary's (key, value) tuple pairs.
    return {key: val for key, val in a_dictionary.items() if val != True}
