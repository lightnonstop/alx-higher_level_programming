#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import hidden_4
    variables = dir(hidden_4)
    for name in variables:
        if name[:2] != '__':
            print(name)
