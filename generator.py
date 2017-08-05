#Generator Functions
#They are coded as normal def but use yield to return results one at a time, suspending and resumin.
#Generator expressions 
#These are similar to the list comprehensions. But they return an object that produces results on demand instead of building a result list.

#neither of them constructs a result list all at once, they save memory space and allow computation time to be split by implementing the iteration protocol.

#Generator Function
def cube(n):
  for i in range(n):
    yield i ** 3

for i in cube(5):
  print(i,end=":")          #":" separeted Ouptut

print("\n")
print(list(cube(5)))        #Output in List format

print("\n")
x = cube(5)
print("-------------------------")
print(iter(x) is x)         #Same as File Iterator, So no need of iter(g)
for i in x:
  print(i,end=":")          #":" separeted Ouptut

print("\n")
print(list(x))              #empty List

print("\n")
#Generator expressions
g = (i ** 3 for i in range(5))

print("-------------------------")
print(iter(g) is g)         #Same as File Iterator, So no need of iter(g)

for i in g:
  print(i, end=":")
  
print("\n")  
print(list(g))              #empty list
print(list((i ** 3 for i in range(5))))            #Output in List format


