
def fun():
  return 1
  return 2
  return 3
  
#for i in fun():     #Object is not Iterable Throw Error
#  print(i)

#Yield 
#The yield enables a function to comeback where it left off when it is called again. This is the critical difference from a regular function. A regular function cannot comes back where it left off. The yield keyword helps a function to remember its state
def fun1():
  yield 1 
  yield 2 
  yield 3
  
for i in fun1():    #A generator looks like a function but behaves like an iterator
  print(i)          #fun1() returns generator Object
  
x = fun1()
print(x)            #generator object
print(next(x))      #return value of first object. No Need to convert using iter()
print(next(x))
print(next(x))
print(next(x))      #StopIteration executed as reached limit  
  
