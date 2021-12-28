#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = len(argv)
    if (count - 1) == 0:
        print('{} arguments.'.format(count - 1), end='\n')
    elif (count - 1) == 1:
        print('{} argument:'.format(count - 1), end='\n')
    else:
        print('{} arguments:'.format(count - 1), end='\n')
    for i in range(len(argv)):
        if i >= 1:
            print('{}: {}'.format(i, argv[i], end=''))
