##### Global variable

def myMethod(y):
    global x
    x=5
    print(y)
myMethod("sam")    
print(x)
print("---------")

########################################

# https://www.w3schools.com/python/python_datatypes.asp #
### Getting the data Type
x=35656222554887711  #int
print(type(x))
x=-888835656222554887711  #int
print(type(x))
x=5.11   #float
print(type(x))
x="Sam"  #str
print(type(x))
x=1j  #complex
print(type(x))
x=1+5j  #complex
print(type(x))

x = ["apple", "banana", "cherry"] #list
print(type(x))
x = ("apple", "banana", "cherry") #tuple
print(type(x))
x = range(6) #range
print(type(x))
x = {"name" : "John", "age" : 36} #dict
print(type(x))
x = {"apple", "banana", "cherry"} #set
print(type(x))
x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(type(x))

x = True  #bool
print(type(x))
x = b"Hello"  #bytes
print(type(x))
x = bytearray(5)  #bytearray
print(type(x))
x = memoryview(bytes(5)) #memoryview
print(type(x))
x = None  #NoneType
print(type(x))

print("---------")

########################################
########################################

# Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
#convert from float to complex:
d = complex(y)

print(a, type(a))  #1.0
print(b, type(b))  #2
print(c, type(c))  #(1+0j)
print(d, type(d))  #(1+0j)
print("---------")


########################################
########################################

### Random: Python does not have a random() function to make a random number,
      #   but Python has a built-in module called random that can be used to make random numbers

import random

print(random.randrange(1, 10))
print("---------")

########################################


print("---------")
########################################
