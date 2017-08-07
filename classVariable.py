#We should be careful when changing value of class variable. If we try to change class variable using object, a new instance (or non-static) variable for that particular object is created and this variable shadows the class variables. Below is Python program to demonstrate the same.

# Class for Computer Science Student
class CSStudent:
    stream = 'cse'     # Class Variable 
    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll
 
# Driver program to test the functionality
# Creating objects of CSStudent class
a = CSStudent("Geek", 1)
b = CSStudent("Nerd", 2)
 
print ("Initially")
print ("a.stream =", a.stream)
print ("b.stream =", b.stream )
 
# This thing doesn't change class(static) variable
# Instead creates instance variable for the object
# 'a' that shadows class member.
a.stream = "ece"
 
print ("\nAfter changing a.stream")
print ("a.stream =", a.stream)
print ("b.stream =", b.stream)

#We should change class variables using class name only.

# Program to show how to make changes to the
# class variable in Python
 
# Class for Computer Science Student
class CSStudent:
    stream = 'cse'     # Class Variable 
    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll
 
# New object for further implementation
a = CSStudent("check", 3)
print ("a.tream =", a.stream)
 
# Correct way to change the value of class variable
CSStudent.stream = "mec"
print ("\nClass variable changes to mec")
 
# New object for further implementation
b = CSStudent("carter", 4)
 
print ("\nValue of variable steam for each object")
print ("a.stream =", a.stream)
print ("b.stream =", b.stream)
