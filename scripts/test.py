import sys;

def biglogs():
    print("im logging a log")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
