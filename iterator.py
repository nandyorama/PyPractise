#List Iterator
x =[1,2,3,4]                #Iterable
print(iter(x) is x)         #x is not an Iterator Object 
xi = iter(x)                #Iterator = iter(Iterable) Manually
print(xi)
print(type(xi))
print(next(xi))             #Value = next(Iterator)
print(next(xi))
print(next(xi))
print(next(xi))
#print(next(xi))            #StopIteration as limit reached

#Iteration tool i.e for loop Implicitly call iter funcition
print("***foor Loop***")
for i in x:
  print(i)

#File Iterator
f = open('Test.txt')
print(iter(f) is f)         #f is an Iterator Object Difference Between File and List Iterator
print(f)
print(type(f))
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))
for f in open('Test.txt'):
  print(f,end='')           #end='' for removing extra New Line
  
print("\n")
D = {'a':12,'b':13,'c':14}
for i in D:                 #Dictionary
  print(i,  D[i])
