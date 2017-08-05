#First Class Function
#It means Function can be assigned, passed as argument and return from function

#Normal Function Assignment
def square(num):
  return num*num

fun = square(5)   #Normal Function call, executed
print(fun)        #Output is 25

#Function assigned as variable
fun = square      #Assigned, not executed
print(fun)        #Function Address
print(square)     #Function Address
print(fun(5))     #Executed function 

#Function passed as an argument
def squareF(num):
	return num*num
 
def cubeF(num):
	return num*num*num;
 
def my_map(func,arg):                 #Function passed as an argument
	res=[]
	for i in arg:
		res.append(func(i))
	return res
 
print("Passing Function as an argument")	
sq = my_map(squareF,[1,2,3,4,5])      #Function passed as an argument	
print(sq)
cb = my_map(cubeF,[1,2,3,4,5])	      #Function passed as an argument
print(cb)

#Function returned from Function
def logger(msg):
  def wrap():
    print("log..{0}".format(msg))
  return wrap
  
log = logger("Passed as an argument to function")
log()                                 #Option1 way of calling function

log = logger
log("Another way")                    #Not Executed Inner function yet i.e wrap
log("Another way")()                  #Option2 way of calling function

#Use of Returning function
def html_tag(tag):
	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag,msg))
	return wrap_text
print_h = html_tag('h1')
print("Returning Function")
print_h("Hello World")
print_h('Welcome')

print_p = html_tag('p')
print_p("How are you")
