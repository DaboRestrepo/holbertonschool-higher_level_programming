#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    argv = sys.argv
    if len(argv) < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        if operator == '+':
            print('{} {} {} = {}'.format(a, operator, b, calc.add(a, b)))
        elif operator == '-':
            print('{} {} {} = {}'.format(a, operator, b, calc.sub(a, b)))
        elif operator == '*':
            print('{} {} {} = {}'.format(a, operator, b, calc.mul(a, b)))
        elif operator == '/':
            print('{} {} {} = {}'.format(a, operator, b, calc.div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
