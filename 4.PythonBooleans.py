
### Booleans represent one of two values: True or False. ####

### The bool() function allows you to evaluate any value,
###     ~ and give you True or False in return,

################################################################################
################################################################################

print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
print("---------")

################################################################################
################################################################################

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print("---------")

################################################################################
################################################################################

## bool() function evaluates any value! >>>>>>>>>>>
# Most Values are True
# ~ Almost any value is evaluated to True if it has some sort of content.
# ~ Any string is True, except empty strings.
# ~ Any number is True, except 0.
# ~ Any list, tuple, set, and dictionary are True, except empty ones.
# ~ In fact, there are not many values that evaluate to False,
#     except empty values, such as (), [], {}, "", the number 0,
#     and the value None.
# ~ And of course the value False evaluates to False.


print(bool("Hello")) #True
print(bool(15)) #True

print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True

print(bool(False)) #False
print(bool(None)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False

print("---------")


# ~ One more value, or object in this case, evaluates to False,
#    and that is if you have an object that is made from a class with
#    a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #False
print("---------")

################################################################################
################################################################################

# Functions can Return a Boolean >>>>>>

def myFunc():
    return True
print(myFunc()) #True
print("---------")

# Print "YES!" if the function returns True, otherwise print "NO!":
class Abc:
    def fn1():
        return True;
myObj = Abc()
if(myObj.fn1):
    print("Yesssss!") #Yesssss!
else:
    print("Noooooo!")


def myFunc():
    return False
if myFunc():
    print("Yes!")
    print("Yippee!")
else:
    print("No!")
    print("Nah!")
print("---------")

################################################################################
################################################################################

# Python also has many built-in functions that return a boolean value,
# ~ like the isinstance() function,
# ~ which can be used to determine if an object is of a certain data type >>>>>>


x=10
print(isinstance(x, int)) #True
print("---------")

################################################################################
################################################################################
