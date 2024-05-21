#!/usr/bin/python3
"""indents text"""


def text_indentation(text):
    """
    prints text with 2 newline after '.' '?' and ':'
    text must be a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = 0
    for i in text:
        if x == 0:
            if i == ' ':
                continue
            x = 1

        if x == 1:
            if i in ".?:":
                print(i + '\n')
                x = 0
            else:
                print (i, end='')
