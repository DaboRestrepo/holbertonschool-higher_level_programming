#!/usr/bin/python3
def safe_print_integer(value):
    if value is not None:
        try:
            value = int(value)
            print("{:d}".format(value))
            return True
        except ValueError:
            return False
