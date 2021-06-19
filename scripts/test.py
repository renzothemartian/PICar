import sys;

# Invoke function as is
def status():
    print("you checked status")


# Take input from cli; pass as arg
def input(mystring):
    print(mystring)



status()







if __name__ == '__main__':
    if sys.argv[1] == 'status':
        globals()[sys.argv[1]]()
    else:
        globals()[sys.argv[1]](sys.argv[2])
