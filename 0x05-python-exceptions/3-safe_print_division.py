#!/usr/bin/python3
def safe_print_division(a, b):
    mul = 0
    try:
        mul = a / b
        return mul
    except ZeroDivisionError:
        mul = None
    finally:
        print("Inside result: {}".format(mul))
