################################################################################
################################################################################

### ------------------------------
### Python - Access List Items >>>>>>>>>>
### ------------------------------

#~ The first item has index 0.
#~ Negative indexing means start from the end
#  e.g. -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1]) #banana
print(thislist[-1]) #mango
#Search will start at index 2(included) & end at index 5(not included).
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']


# Check if Item Exists >>>>
# ~ To determine if a specified item is present in a list use the in keyword

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print("---------")


################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Change List Items >>>>>>>>>>
### ------------------------------

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon']

# If you insert more items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #Change the second value by replacing it with two new values
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

# If you insert less items than you replace, the new items will be inserted where you specified,
#  and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] #Change the second and third value by replacing it with one value
print(thislist) #['apple', 'watermelon']
thislist[1:500] = ["watermelon2"]
print(thislist) #['apple', 'watermelon2']

print("---------")



################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Add List Items >>>>>>>>>>
### ------------------------------

### APPROACH-1 ###
# Append Items  >>>>
#  ~ To add an item to the end of the list, use the append() method

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") 
print(thislist) #['apple', 'banana', 'cherry', 'orange']


### APPROACH-2 ###
# Insert Items >>>>
# ~ To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# ~ The insert() method inserts an item at the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #Insert "watermelon" as the third item
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']
print("---------")


### APPROACH-3 ###
# Extend List  >>>>
# ~ To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #Add the elements of tropical to thislist
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# ~ Add Any Iterable in extend() >>
#   ~ The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #Add elements of a tuple to a list
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

print("---------")

################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Remove List Items >>>>>>>>>>
### ------------------------------

# ~ The remove() method removes the specified item
# ~ If there are more than one item with the specified value, the remove() method removes the first occurance

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #Remove the first occurance of "banana"
print(thislist) #['apple', 'cherry', 'banana', 'kiwi']


# Remove Specified Index >>>>>
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Remove the second item
print(thislist) #['apple', 'cherry']
#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop() #Remove the last item
print(thislist) #['apple', 'banana']


# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist #Delete the entire list
#print(thislist)

# The clear() method empties the list.
# ~ The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear() #Clear the list content
print(thislist) #[]

print("---------")
################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Loop Lists >>>>>>>>>>
### ------------------------------

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Loop Through the Index Numbers >>>>
  #~ You can also loop through the list items by referring to their index number.
  #~ Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# While loop >>>>
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Looping Using List Comprehension >>>>
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #A short hand for loop that will print all items in a list

print("---------")


################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - List Comprehension >>>>>>>>>>
### ------------------------------
"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
    Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
    Without list comprehension you will have to write a for statement with a conditional test inside
"""
### APPROACH-1 for example ###
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

### APPROACH-2 for example ### *** Imp!! ***
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #With list comprehension you can do all that with only one line of code
print(newlist)

#---------------------------
"""
SYNTAX: newlist = [expression for item in iterable if condition == True]
Note: The return value is a new list, leaving the old list unchanged.
"""
#---------------------------

### A. Condition ###
#~ The condition is like a filter that only accepts the items that valuate to True

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"] #Only accept items that are not "apple"
print(newlist) #['banana', 'cherry', 'kiwi', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)


### B. Iterable ###
#~ The iterable can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in range(10)]
print(newlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist) #[0, 1, 2, 3, 4]



### C. Expression ###
#~ The expression is the current item in the iteration, but it is also the outcome,
#~   which you can manipulate before it ends up like a list item in the new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits] #Set the values in the new list to upper case
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits] #Set all values in the new list to 'hello'
print(newlist) #['hello', 'hello', 'hello', 'hello', 'hello']

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
# ~ e.g. "Return the item if it is not banana, if it is banana return orange".
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana"
print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']


print("---------")


################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Sort Lists >>>>>>>>>>
### ------------------------------

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #Sort the list alphabetically
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort() #Sort the list numerically
print(thislist) #[23, 50, 65, 82, 100]


# Sort Descending >>>>>>
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #To sort descending, use the keyword argument reverse = True
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #[100, 82, 65, 50, 23]

print("---------")

# Customize Sort Function >>>>>>>>>>>> ******** Imp **********
# ~ You can also customize your own function by using the keyword argument key = function.
# ~ The function will return a number that will be used to sort the list (the lowest number first)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #Sort the list based on how close the number is to 50
print(thislist) #[50, 65, 23, 82, 100]


# Case Insensitive Sort >>>>>
# ~ By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() #Case sensitive sorting can give an unexpected result
print(thislist) #['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #Luckily we can use built-in functions as key functions when sorting a list. So if you want a case-insensitive sort function, use str.lower as a key function.
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']


# Reverse Order >>>>
# ~ The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']

################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Copy Lists >>>>>>>>>>
### ------------------------------
"""
You cannot copy a list simply by typing list2 = list1.
Because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy()
"""
### APPROACH-1 ###

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #Make a copy of a list with the copy() method
print(mylist)

### APPROACH-2 ###
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #Another way to make a copy is to use the built-in method list().
print(mylist)


print("---------")


################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Join Lists >>>>>>>>>>
### ------------------------------

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

### APPROACH-1 ###
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


### APPROACH-2 ###
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x) #Another way to join two lists is by appending all the items from list2 into list1, one by one

print(list1)


### APPROACH-3 ###
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #Use the extend() method to add list2 at the end of list1
print(list1)

print("---------")

################################################################################
################################################################################
################################################################################
################################################################################

### ------------------------------
### Python - Lists Methods >>>>>>>>>>
### ------------------------------


"""
Python has a set of built-in methods that you can use on lists.

Method	        Description
append()	Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	        Sorts the list
"""


print("---------")


################################################################################
################################################################################

