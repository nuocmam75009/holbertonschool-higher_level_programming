#!/usr/bin/python3
import sys

def add_all_args(args):
    return sum(int(arg) for arg in args)

if __name__ == "__main__":
    print(add_all_args(sys.argv[1:]))
