import sys;

# def biglogs():
#     print("im logging a log")

# if __name__ == '__main__':
#     globals()[sys.argv[1]]()

# Take input from cli; pass as arg
def input(mystring):
    print(mystring)


if __name__ == '__main__':
    if sys.argv[1] == 'biglogs':
        globals()[sys.argv[1]]()
    else:
        globals()[sys.argv[1]](sys.argv[2])
