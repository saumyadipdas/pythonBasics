
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
print("---------")

a = " Hello, World! " #Remove Whitespace
print(a.strip()) # returns "Hello, World!"
print("---------")

a = "Hello, World!" #Replace String
print(a.replace("H", "J"))


########################################

# Split Strings

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print("---------")


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

## Example >>> ##

a="A\\BC\"D"
print(a)
print(len(a))
a="AbCdE"
print(a.upper())
print(a.lower())
print(a[:2])
a="  hello,world  "
print(a.strip().split(","))
print("---------")
price = 59.32923
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)

################################################################################
################################################################################
