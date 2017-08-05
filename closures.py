#Example Of Closures
def outer():          #Outer Function
	msg = "HI"
	def inner():        #Inner Function inside Outer Function
		print(msg)
	return inner()      #Executing inner function
 
outer()               #executing outer function->inner function ->Prints HI
print("-------------------------------")

def outerF():
	msg = "Hello"
	def innerF():
		print(msg)
	return innerF #Not Executing function
 
outerF()              #No Output as not executed yet	
my_func = outerF()
print(my_func)  			#Prints Function Object
print("Inner Function name is ", my_func.__name__)#Prints Inner function Name i.e "inner"
my_func()     				#Executes innner function->Print msg
print("-------------------------------")

def outerFF(m):
	msg = m
	def innerFF():
		print(msg)
	return innerFF      #Not Executing function
 
hi_func = outerFF("Hi")
hello_func = outerFF("Hello")
hi_func()
hello_func()
