#!/usr/bin/python3
import sys

def print_args(args):
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_args(sys.argv[1:])