#!/usr/bin/python3
def no_c(my_string):
    return ''.join([i for i in my_string if i not in ['c', 'C']])