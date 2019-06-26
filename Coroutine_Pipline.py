import time
def coroutine(func):
	print("******In coroutine*********")
	def start(*args,**kwargs):
		cr = func(*args,**kwargs)
		next(cr)
		return cr
	return start

def follow(file,target):
    #file.seek(0,2)
    print("******In follow*********")
    while True:
        line = file.readline()
        #print(line)
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

@coroutine    
def broadcast(targets):
    print("******In broadcast*********")
    while True:
        item = yield
        for target in targets:
            target.send(item)

@coroutine
def grep(pattern,target):
    print("******In grep*********")
    while True:
        line = yield
        if pattern in line:
            #print(line)
            target.send(line)
            
@coroutine
def prnter():
    print("******In prnter*********")
    while True:
        line = yield
        print(line)
            
f = open("access.txt")
follow(f,broadcast([grep("python",prnter()),grep("hello",prnter()),grep("blr",prnter())]))
