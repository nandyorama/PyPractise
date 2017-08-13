#Property Decorator
#eaxmple 4 Using Property Decorator with setter
class Employee:
  def __init__(self,first,last):
    self.first = first
    self.last = last
    
  @property # access method as attribute
  def email(self):
    return "{}.{}@gmail.com".format(self.first ,self.last)
  
  @property # access method as attribute
  def fullName(self):
    return "{} {}".format(self.first,self.last)
  
  @fullName.setter
  def fullname(self,name):
    first , last = name.split(" ")
    self.first = first
    self.last = last
    
emp = Employee("John","smith")

emp.fullname = "pramod kumar"

print(emp.first)
print(emp.email)  #email is taking proper first Name with property decorator
print(emp.fullName)

#example 3 Using Property Decorator
"""
class Employee:
  def __init__(self,first,last):
    self.first = first
    self.last = last
    
  @property # access method as attribute
  def email(self):
    return "{}.{}@gmail.com".format(self.first ,self.last)
  
  @property # access method as attribute
  def fullName(self):
    return "{} {}".format(self.first,self.last)
  
emp = Employee("John","smith")

emp.first = "jim"

print(emp.first)
print(emp.email)  #email is taking proper first Name with property decorator
print(emp.fullName)
"""

#example 2 Using email function
"""
class Employee:
  def __init__(self,first,last):
    self.first = first
    self.last = last
  
  def email(self):
    return "{}.{}@gmail.com".format(self.first ,self.last)
  
  def fullName(self):
    return "{} {}".format(self.first,self.last)
  
emp = Employee("John","smith")

emp.first = "jim"

print(emp.first)
print(emp.email())  #email is taking proper first Name with email function
print(emp.fullName())
"""

#example1
"""
class Employee:
  def __init__(self,first,last):
    self.first = first
    self.last = last
    self.email = first +"."+last+"@gmail.com"
  
  def fullName(self):
    return "{} {}".format(self.first,self.last)
  
emp = Employee("John","smith")

emp.first = "jim"

print(emp.first)
print(emp.email)  #email is not taking proper first Name
print(emp.fullName())
"""
