#!/usr/bin/python3
from "hidden_4" import

if __name__ == "__main__":
    names = [name for name in dir(hidden_4) if not name.startswith('__')]
    for name in sorted(names):
        print(name)