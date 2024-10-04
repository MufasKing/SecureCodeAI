import os

def open_file(filename, mode):
    if mode == 'w':
        os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY | os.O_EXCL)
    else:
        os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_WRONLY)

def main():
    open_file('test.txt', 'w')
    open_file('test.txt', 'r')

if __name__ == '__main__':
    main()