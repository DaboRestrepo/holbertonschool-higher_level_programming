#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = abs(number) % 10
if number < 0:
    mod = -mod
    print('Last digit of', number, 'is', mod, 'and is less than 6 and not 0')
elif mod == 0:
    print('Last digit of', number, 'is', mod, 'and is 0')
elif mod > 5:
    print('Last digit of', number, 'is', mod, 'and is greater than 5')
else:
    print('Last digit of', number, 'is', mod, 'and is less than 6 and not 0')
