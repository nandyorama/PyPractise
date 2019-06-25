import time
def coroutine(func):
    #print("******In coroutine*********")
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start

@coroutine
def tail(file,target):
    #print("******In Tail*********")
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

@coroutine
def grep(pattern,target):
    #print("******In Grep*********")
    while True:
        line = yield
        if pattern in line:
            #print(line)
            target.send(line)

@coroutine
def printer():
    #print("******In Printer*********")
    while True:
        line = yield
        print(line)

            
file = open("access.txt")
tail(file,grep("python",printer()))
