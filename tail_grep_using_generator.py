import time

#tail -f | grep Using Generator
def tail(file):
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line 

def grep(lines,pattern):
    for line in lines:
        if pattern in line:
            yield line
            
            
logf = open("access.txt")
files = tail(logf)
lines = grep(files,"python")
for line in lines:
    print(line)
