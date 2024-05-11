################### ################### ################### 
################### $$$ Python Lists $$$ ###################
################### ################### ###################

"""
# Python Collections (Arrays) >>>>>>>>>
# There are four collection data types in the Python programming language:
# -----------------------------------------------------------------------

~ List is a collection which is ordered and changeable. Allows duplicate members.
~ Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
~ Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
~ Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""


"""
Lists are one of 4 built-in data types in Python used to store collections of data.
The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

~ Lists are used to store multiple items in a single variable.
~ Lists are created using square brackets.
~ List items are ordered, changeable, and allow duplicate values.
~ List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

################################################################################
################################################################################
################################################################################
################################################################################

## Just trying Python Class & Objects ***** ## (Just for knowledge)
if 2>3:
    print("1")
elif 3>2:
    print("2")
else:
    print("3")

class Abc:
    def myFunc(self):
        print("Inside func")
a = Abc()
a.myFunc() 

print("---------")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the properties 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area() #Area of Room = 1309.0
print("---------")

################################################################################
################################################################################
################################################################################
################################################################################

thislist = ["apple", "banana", "cherry"]
print(thislist)

print("---------")
print("---------")

################################################################################
################################################################################

#List Length  >>>>>>>>>>
#To determine how many items a list has, use the len() function

myList = ["A", "B", "C"]
print(len(myList))
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print("---------")
################################################################################
################################################################################

# List items can be of any data type  >>>>>>>>>>

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
print("---------")


################################################################################
################################################################################

# type()  >>>>>>>>>>
## From Python's perspective, lists are defined as objects with the data type 'list'

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #<class 'list'>
print("---------")


################################################################################
################################################################################

# The list() Constructor >>>>>>>>>>
# ~ It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(thislist)
print("---------")


################################################################################
################################################################################



print("---------")


################################################################################
################################################################################


