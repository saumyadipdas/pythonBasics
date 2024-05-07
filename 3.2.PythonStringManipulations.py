
########################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python - Slicing Strings ##########################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

b = "ABCDEFGHIJK!"
print(b[2:5]) #Get the characters from position 2 to position 5 (not included)
print("---------") #O/P: CDE


########################################

# Slice From the Start
# (Note: The first character has index 0.)

b = "Hello, World!"
print(b[:5]) #Get the characters from the start to position 5 (not included)
print("---------") #O/P: Hello

# Slice To the End
b = "Hello, World!"
print(b[2:]) #Get the characters from position 2, and all the way to the end
print("---------") #O/P: llo, World!

########################################

# Negative Indexing
# Use negative indexes to start the slice from the end of the string

b = "Hello, World!"
print(b[-5:-2]) #From: "o" in "World!" (position -5),
                #To, but not included: "d" in "World!" (position -2):
print("---------") #O/P: orl

################################################################################
################################################################################
################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python - Modify Strings ##########################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.swapcase()) #Swap Case
print("---------")

a = " Hello, World! " #Remove Whitespace
print(a.strip()) # returns "Hello, World!"
print("---------")

a = "Hello, World!" #Replace String
print(a.replace("H", "J"))

################################################################################
################################################################################
################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# title() method ##########################
# Make the first letter in each word upper case
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
txt = "Welcome to my 2nd world"
x = txt.title()
print(x) #Welcome To My 2Nd World

#Note that the first letter after a non-alphabet letter is converted into a upper case letter
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x) #Hello B2B2B2 And 3G3G3G

################################################################################
################################################################################
################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# replace() method ##########################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2) #Replace the two first occurrence of the word "one"
print(x) #three three was a race horse, two two was one too.

################################################################################
################################################################################
################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# startswith() method ##########################
# The startswith() method returns True if the string starts with the specified value, otherwise False.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   

txt = "Hello, welcome to my world."
x = txt.startswith("Hello") #Check if the string starts with "Hello"
print(x) #True
x = txt.startswith("wel", 7, 20) #Check if position 7 to 20 starts with the characters "wel"
print(x) #True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# endsWith() >>>>>>>>>>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) #true
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11) #Check if position 5 to 11 ends with the phrase "my world."
print(x) #false
print("---------")


################################################################################
################################################################################
################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Split Strings >>>>>>>>>>>>>>> ##########
# split(), rsplit() & splitlines().
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###### split() >>>>>>>>>>>>>>>>>>>>>>>> Syntax: string.rsplit(separator, maxsplit)

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ") # ['hello', 'my name is Peter', 'I am 26 years old']
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1) # ['apple', 'banana#cherry#orange']
print(x)
print("---------")

########################################

###### rsplit() >>>>>>>>>>>>>>>>>>>>>>>> Syntax: string.rsplit(separator, maxsplit)
# ~ The rsplit() method splits a string into a list, starting from the right.
# ~ If no "max" is specified, this method will return the same as the split() method.
# ~ Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

#   ( maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences" )


txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x) #['apple', 'banana', 'cherry']
x = txt.split(", ")
print(x) #['apple', 'banana', 'cherry']

x = txt.rsplit(", ", 1) ## setting the maxsplit parameter to 1, will return a list with 2 elements!
print(x) #['apple, banana', 'cherry']
x = txt.split(", ", 1)
print(x) #['apple', 'banana, cherry']
x = txt.rsplit(", ", -1) ## Default maxSplit!
print(x) #['apple', 'banana', 'cherry']


########################################

###### splitlines() >>>>>>>>>>>>>>>>>>>>>>>>

x = txt.splitlines(True) #param: Optional. Specifies if the line breaks should be included (True), or not (False). Default value is False
print(x) #['Thank you for the music\n', 'Welcome to the jungle']

## splitlines() : Split a string into a list where each line is a list item. The splitting is done at line breaks.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x) #['Thank you for the music', 'Welcome to the jungle']

################################################################################
################################################################################
################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String Concatenation ##########################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a = "Hello"
b = "World"
c = a + b
print(c)
print("---------")

################################################################################
################################################################################
################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python - Format - Strings ##########################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# we cannot combine strings and numbers like this
age = 36
#txt = "My name is John, I am " + age
#print(txt)
#print("---------")

## But we can combine strings and numbers by using f-strings or the format() method!

## F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# ~ To specify a string as an f-string, simply put an f in front of the string literal,
# ~ and add curly brackets {} as placeholders for variables and other operations.

age = 36
txt = f"My name is John, I am {age}"
print(txt)
print("---------")
price = 59
txt = f"The price is {price} dollars"
print(txt)
print("---------")

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
price = 59.32923
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)
print("---------")

################################################################################
################################################################################
################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python - Escape Characters ##########################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
a = "Hello\nWorld"
print(a)
a = "Hello\\World"
print(a)
a = "Hello\rWorld"
print(a)
a = "Hello\tWorld"
print(a)
a = "Hello \bWorld!"
print(a)
print("---------")


################################################################################
################################################################################
################################################################################
################################################################################

## Example >>> ##

a="A\\BC\"D"
print(a) #A\BC"D
print(len(a)) #6
print("---------")
a="AbCdE"
print(a.upper()) #ABCDE
print(a.lower()) #abcde
print(a.swapcase()) #aBcDe
txt = "Welcome to my 2nd world"
x = txt.title()
print(x) #Welcome To My 2Nd World
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2) #Replace the two first occurrence of the word "one"
print(x) #three three was a race horse, two two was one too.
print("---------")
print(a[:2]) #Ab
a="  hello,world  "
print(a.strip().split(",")) #['hello', 'world']
print("---------")
price = 59.32923
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)
print("---------")

################################################################################
################################################################################
