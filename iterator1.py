#Input n Print Numbers in reverse Order
class rrange:
  def __init__(self,n):
    self.index = n 
    self.num = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    self.num = self.index
    self.index -= 1
    if self.index < 0:
      raise StopIteration
    return self.num
      
print("Using For Loop----")
for i in rrange(5):
  print(i)

print("Using Next--------")
rr = rrange(5)
itr = iter(rr)
print(next(itr))
print(next(itr))                 
print(next(itr))
print(next(itr))
print(next(itr))                 
#print(next(itr))              #StopIteration Executed as limit reached

#Input List, Print list in Order
class lrange:
  def __init__(self,lst):
    self.lst = lst
    self.index = len(self.lst)
    self.num = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    self.num = self.index-1
    self.index -= 1
    if self.index < 0:
      raise StopIteration
    return self.lst[self.num]

lr = lrange([11,12,13,14,15]) 
print(list(lr))               #Print using list

for i in lrange([11,12,13,14,15]):
  print(i)

    
    
    
