#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int): #check if it's an int
                print("{:d}".format(my_list[i]), end='')
                number += 1
        print()
    except IndexError:
        print("")
    return number
