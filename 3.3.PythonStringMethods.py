################################################################################
################################################################################
################################################################################

###### <<< String METHODS >>> ######

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

################################################################################
################################################################################
################################################################################

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
print("---------")

################################################################################
################################################################################
################################################################################

# capitalize, casefold, lower  >>>>>>>>>>

a="abcdEFGH"
print(a.capitalize()) #Abcdefgh
print(a.casefold()) #abcdefgh
print(a.lower()) #abcdefgh
print("---------")

########################################

# center(): Returns a centered string  >>>>>>>>>>

txt = "banana"
x = txt.center(10, "X") #XXbananaXX
print(x)
print("---------")

########################################

# count()  >>>>>>>>>>

#Return the number of times the value "apple" appears in the string
txt = "I love apples, apple are my favorite fruit. apple is my apple."
x = txt.count("apple")
print(x) #2
#Search from position 10 to 24
txt = "I love apples, apple are my favorite fruit. apple is my apple."
x = txt.count("apple", 10, 24) #string.count(value, start, end)
print(x) #1
print("---------")


########################################

# String encode() Method >>>>>>>>>>

txt = "My name is Ståle"
x = txt.encode()#UTF-8 encode the string
print(x)
print("---------")
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print("---------")


########################################

# endsWith() >>>>>>>>>>

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) #true
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11) #Check if position 5 to 11 ends with the phrase "my world."
print(x) #false
print("---------")

########################################

# expandtabs() : A number specifying the tabsize. Default tabsize is 8 >>>>>>>>>>

txt = "H\te\tl\tl\to"
print(txt)                  #H	     e	     l	     l	     o
print(txt.expandtabs())     #H       e       l       l       o
print(txt.expandtabs(1))    #H e l l o
print(txt.expandtabs(2))    #H e l l o
print(txt.expandtabs(4))    #H   e   l   l   o
print(txt.expandtabs(10))   #H         e         l         l         o
print("---------")


########################################

# find() method >>>>>>>>>>

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?
x = txt.find("e", 5, 10)
print(x)

#If the value is not found, the find() method returns -1, but the index() method will raise an exception
print(txt.find("q"))  # -1
#print(txt.index("q")) # Exception
print(txt.index("e")) # 1
print("---------")


########################################

# format() method >>>>>>>>>>

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
# The Placeholders
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
print("---------")

########################################

# index() method >>>>>>>>>>
#  ~ The index() method is almost the same as the find() method,
#  ~ the only difference is that the find() method returns -1 if the value is not found.

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x) #1
print("---------")

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################


# isalnum(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(),  >>>>>>>>>>
# isprintable(), isspace(), istitle(), isupper() methods >>>>>>>>>>

#The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# ~ Example of characters that are not alphanumeric: (space)!#%&? etc
txt = "Company 12"
x = txt.isalnum()
print(x) #False

#The isalpha() method returns True if all the characters are alphabet letters (a-z)
x = txt.isalpha()
print(x) #False

#The isascii() method returns True if all the characters are ascii characters  (a-z)
x = txt.isascii()
print(x) #True

#The isdecimal() method returns True if all the characters are decimals (0-9)
txt = "1234"
x = txt.isdecimal()
print(x) #True
a = "\u0030" #unicode for 0 (zero)
b = "\u0047" #unicode for G
print(a.isdecimal()) #True
print(b.isdecimal()) #False

#The isdigit() method returns True if all the characters are digits, otherwise False
a = "\u0030" #unicode for 0 (zero)
b = "\u00B2" #unicode for ²
print(a.isdigit()) #True
print(b.isdigit()) #True

#The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# ~ A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_)
# ~ A valid identifier cannot start with a number, or contain any spaces.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier()) #True
print(b.isidentifier()) #True
print(c.isidentifier()) #False
print(d.isidentifier()) #False
print("---------")

#The islower() method returns True if all the characters are in lower case, otherwise False.
# ~ Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "hello world!"
x = txt.islower()
print(x)
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())


#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# ~ Exponents, like ² and ¾ are also considered to be numeric values.
# ~ "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())


#The isprintable() method returns True if all the characters are printable, otherwise False.
# ~ Example of none printable character can be carriage return and line feed.

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)


#The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
txt = "   s   "
x = txt.isspace()
print(x)


#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


#The isupper() method returns True if all the characters are in upper case, otherwise False.
# ~ Numbers, symbols and spaces are not checked, only alphabet characters.
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())
print(b.isupper())
print(c.isupper())

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################

# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################


# XXX() method >>>>>>>>>>


print("---------")

########################################
########################################


