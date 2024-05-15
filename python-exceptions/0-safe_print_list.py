#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            number += 1
            print()
    except IndexError:
        print()
    return number
# try lets you test a block of code
# except lets you handle the error
