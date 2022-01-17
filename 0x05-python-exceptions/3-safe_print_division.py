#!/usr/bin/python3
def safe_print_division(a, b):
    mul = 0
    try:
        mul = a / b
        return mul
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(mul))
