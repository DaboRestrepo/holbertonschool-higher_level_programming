#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4 as file
    for i in dir(file):
        if i[0:2] != '__':
            print('{}'.format(i), end='\n')
