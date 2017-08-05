#Print Numbers Using Iterator
class crange:
  def __init__(self,n):
    self.index = n 
    self.num = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.num <= self.index:
      self.num += 1
      return self.num
    else:
      raise StopIteration

cr = crange(5)
print(list(cr))
print(list(cr))                 #Output is empty List
print(list(cr))

#Print Number using Nested Iterator
class ncrange:
  def __init__(self,n):
    self.index = n 

  def __iter__(self):
    return crange(self.index)
  
ncr = ncrange(5)
print(list(ncr))
print(list(ncr))                #Output is not empty
print(list(ncr))
















