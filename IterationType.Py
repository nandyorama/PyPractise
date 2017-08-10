lst = [1,2,3]
#print(dir(lst))  #All default Methods
print("List Iteration Using For Loop")
for i in lst:
  print(i)
  
print("Iteration Using Iterator")  
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #Exception StopIteration



#square of Input List
#Option 1 Square Function appending to List and return it.
def square(inputlst):
  op = []
  for i in inputlst:
    op.append(i*i)
  return op

print("Square Function of Input List")  
result = square(lst)
print(result)
    
#Option 2 Using List expression
print("Using List expression")
res = [x*x for x in lst]
print(res)

#Option 3 Using Genrator expression
print("Using Generator expression")
resGen = (x*x for x in lst)
print(resGen)   #Not output list but Generator Object
for i in resGen:#Using loop to iterate Generator
  print(i)

#print(list(resGen))    #Performance of Generator is lost by using list

#Option 4 Using Genrator function
def squareG(inputlst):
  for i in inputlst:
    yield(i*i)

print("Square Generator Function with loop")
for i in squareG(lst):#Using loop to iterate Generator
  print(i)

print("Square Generator Function with Iterator")
result = squareG(lst)
print(iter(result) is result)
print(next(result))
print(next(result))
print(next(result))
#print(next(result))  #StopIteration as limit reached

#Option 5 Using Genrator function without yield
class SQ:
  def __init__(self,lst):
    self.lst = lst
    self.len = len(lst)
    self.num = 0
    
  def __iter__(self):
    return self
    
  def __next__(self):
    self.num += 1
    if self.num <= self.len:
      return (self.lst[self.num-1]*self.lst[self.num-1])
    else:
      raise StopIteration
      
print("Using Genrator function without yield")      
sq = SQ(lst)
sqi = iter(sq)
print(next(sqi))
print(next(sqi))
print(next(sqi))
#print(next(sqi)) #StopIteration    


  

