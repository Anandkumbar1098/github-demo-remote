#ADD implementation
def add(x,y):
    return x+y

#Substract implementation    
def substract(x,y):
    return x-y          # on master

#Multiply implementation    
def multiply(x,y):
    return x*y          # on Bug456

#Divide implementation
def divide(x,y):
    if(y==0):           # on Bug789
        return "Divide By 0 Error"
    else:
        return x/y
#square implementation      
def square(x):
    return x*x

