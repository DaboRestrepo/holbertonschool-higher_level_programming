#!/usr/bin/python3
from typing import Counter


if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = 0
    for i in range(len(argv)):
        count = count + 1
    print('{} arguments.'.format(count - 1), end='\n')
    for i in range(len(argv)):
        if i >= 1:
            print('{}: {}'.format(i, argv[i], end=''))
