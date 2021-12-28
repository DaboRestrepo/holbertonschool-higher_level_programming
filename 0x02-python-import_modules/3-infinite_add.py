#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = len(argv)
    sum = 0
    for i in range(count):
        if i >= 1:
            sum = sum + int(argv[i])
    print('{}'.format(sum))
