#decorator function
#example4 Class Decorator
class dClass(object):
	def __init__(self,oFunc):
		self.oFunc = oFunc
 
	def __call__(self,*args):
		print("Class Executed before {}".format(self.oFunc.__name__))
		return self.oFunc(*args)
 
@dClass	
def display4():
	print("Welcome to Decorator4")
 
@dClass	
def display_info4(name,age):
	print("Person Detail are {}{}".format(name,age))
 
display_info4("Ram",20)
display4()	
 
print("\n\n")
print("*****************************")
 
#example3 Function Decorator
def dFunc2(oFunc):
	def wFunc(*args):
		print("Wrapper Executed before {}".format(oFunc.__name__))
		return oFunc(*args)
	return wFunc
 
@dFunc2	
def display2():
	print("Welcome to Decorator3")
 
@dFunc2	
def display_info(name,age):
	print("Person Detail are {}{}".format(name,age))
 
display_info("Ram",20)
display2()	
 
print("\n\n")
print("-------------------")
 
#example2
def dFunc1(oFunc):
	def wFunc():
		print("Wrapper Executed before {}".format(oFunc.__name__))
		return oFunc()
	return wFunc
 
@dFunc1	
def display1():
	print("Welcome to Decorator2")
 
display1()	
 
#example1
def dFunc(oFunc):
	def wFunc():
		return oFunc()
	return wFunc
 
def display():
	print("Welcome to Decorator")
 
dec_func = dFunc(display)
dec_func()
