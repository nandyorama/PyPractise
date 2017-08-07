# Accessing items using enumerate()
 
cars = ["Aston" , "Audi", "McLaren "]
for i, x in enumerate(cars):
    print (x)
  
print (list(enumerate(cars)))

for x in enumerate(cars):
    print (x[0],x[1])  
    
#Enumerate takes parameter start which is default set to zero. We can change this parameter to any value we like. In the below code we have used start as 1.

# demonstrating use of start in enumerate
for x in enumerate(cars, start=1):
    print (x[0], x[1])    
    
#enumerate() helps to embed solution for accessing each data item in iterator and fetching index of each data item.    
    
