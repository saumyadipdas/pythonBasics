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
################################################################################

# capitalize, casefold, lower  >>>>>>>>>>

a="abcdEFGH"
print(a.capitalize()) #Abcdefgh
print(a.casefold()) #abcdefgh
print(a.lower()) #abcdefgh
print(a.upper()) #ABCDEFGH
print(a.swapcase()) #ABCDefgh
print("---------")

################################################################################


# center(): Returns a centered string  >>>>>>>>>>

txt = "banana"
x = txt.center(10, "X") #XXbananaXX
print(x)
print("---------")

################################################################################


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

################################################################################
################################################################################

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


################################################################################
################################################################################

# expandtabs() : A number specifying the tabsize. Default tabsize is 8 >>>>>>>>>>

txt = "H\te\tl\tl\to"
print(txt)                  #H	     e	     l	     l	     o
print(txt.expandtabs())     #H       e       l       l       o
print(txt.expandtabs(1))    #H e l l o
print(txt.expandtabs(2))    #H e l l o
print(txt.expandtabs(4))    #H   e   l   l   o
print(txt.expandtabs(10))   #H         e         l         l         o
print("---------")

################################################################################
################################################################################

# find(), index(), rfind(), rindex() method >>>>>>>>>>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) #7

x = txt.find("e", 5, 10) ##Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?
print(x) #8
x = txt.find("e") #Where in the text is the first occurrence of the letter "e"?
print(x) #1

#If the value is not found, the find() method returns -1, but the index() method will raise an exception
print(txt.find("q"))  # -1
#print(txt.index("q")) # Exception
print(txt.index("e")) # 1
print("---------")


### rfind-> The rfind() method finds the last occurrence of the specified value
### ~ The rfind() method returns -1 if the value is not found.
### ~ The rfind() method is almost the same as the rindex() method.

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10) ##Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?
print(x) #8
x = txt.rfind("e") #Where in the text is the last occurrence of the letter "e"?
print(x) #13

print(txt.rfind("q")) # -1
#print(txt.rindex("q")) # Exception
print("---------")

################################################################################
################################################################################

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

################################################################################
################################################################################

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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
print(x) #True
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower()) #False
print(b.islower()) #True
print(c.islower()) #False

#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# ~ Exponents, like ² and ¾ are also considered to be numeric values.
# ~ "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric()) #True
print(b.isnumeric()) #True
print(c.isnumeric()) #False
print(d.isnumeric()) #False
print(e.isnumeric()) #False


#The isprintable() method returns True if all the characters are printable, otherwise False.
# ~ Example of none printable character can be carriage return and line feed.

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) #True


#The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
txt = "   s   "
x = txt.isspace()
print(x) #False


#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle()) #False
print(b.istitle()) #True
print(c.istitle()) #True
print(d.istitle()) #True


#The isupper() method returns True if all the characters are in upper case, otherwise False.
# ~ Numbers, symbols and spaces are not checked, only alphabet characters.
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper()) #False
print(b.isupper()) #False
print(c.isupper()) #True
print("---------")


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

# join() method >>>>>>>>>> [[Joins the elements of an iterable to the end of the string]]
#Syntax: string.join(iterable)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) #John#Peter#Vicky

#Note: When using a dictionary as an iterable,
# ~ the returned values are the keys, not the values.
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x) #nameTESTcountry

print("---------")

################################################################################
################################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### ljust(), rjust(), lstrip(), rstrip(), strip() >>>>>>>>>>>>>>>>>>>>>>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ljust(), lstrip() method >>>>>>>>>>

txt = "banana"
x = txt.ljust(10) ##Return a 10 characters long, left justified version of the word "banana"
print(x, "is my favorite fruit.") #banana     is my favorite fruit.
x = txt.ljust(10, "X") ##Using the letter "X" as the padding character
print(x) #bananaXXXX
print("---------")

txt = "     banana     "
x = txt.lstrip() #Remove spaces to the left of the string
print("of all fruits", x, "is my favorite") #of all fruits banana      is my favorite

#The lstrip() method removes any leading characters (space is the default leading character to remove)
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw") #Remove the leading characters.  Remove the leading characters if they are commas, periods, a, s, or w
print(x) #banana
x = txt.lstrip(",swa")
print(x) #.....banana
x = txt.lstrip(",swa.")
print(x) #banana
print("---------")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# rjust(), rstrip() method >>>>>>>>>>

txt = "banana"
x = txt.rjust(10) ##Return a 10 characters long, right justified version of the word "banana"
print(x, "is my favorite fruit.") #    banana is my favorite fruit.
x = txt.rjust(10, "X") ##Using the letter "X" as the padding character
print(x) #XXXXbanana
print("---------")

txt = "     banana     "
x = txt.rstrip() #Remove spaces to the right of the string
print("of all fruits", x, "is my favorite") #of all fruits      banana is my favorite

#The rstrip() method removes any leading characters (space is the default leading character to remove)
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw") #Remove the leading characters. Remove the trailing characters if they are commas, periods, s, q, or w
print(x) #banana
x = txt.rstrip("q,sw.")
print(x) #banana
x = txt.rstrip(".") #banana,,,,,ssqqqww
x = txt.rstrip(".") #banana,,,,,ssqqqww.....
x = txt.rstrip(".,") #banana,,,,,ssqqqww
x = txt.rstrip(".,wq") #banana,,,,,ss
print("---------")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# strip() method >>>>>>>>>>

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt") #Remove the leading and trailing characters
print(x) #banana


################################################################################
################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# zfill() method >>>>>>>>>>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~ The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
#~ If the value of the len parameter is less than the length of the string, no filling is done.

a = "hello"
b = "welcome to the jungle"
c = "10.000"
#Fill the strings with zeros until they are 10 characters long
print(a.zfill(10)) #00000hello
print(b.zfill(10)) #welcome to the jungle
print(c.zfill(10)) #000010.000
print("---------")


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

     #~~~~ ADVANCED CONCEPTS  ~~~~#

################################################################################
################################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# translate() method >>>>>>>>>>
# [[ Returns a translated string ]]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# ~ Use the maketrans() method to create a mapping table.
# ~ If a character is not specified in the dictionary/table, the character will not be replaced.
# ~ If you use a dictionary, you must use ascii codes instead of characters.


#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80} #Replace any "S" characters with a "P" character
txt = "Hello Sam!"
print(txt.translate(mydict)) #Hello Pam!

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable)) #Hello Pam!
print("---------")

#~~~~~~~~~~~~~~~
#Use a mapping table to replace many characters:
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable)) #Hi Joe!


#The third parameter in the mapping table describes characters that you want to remove from the string
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable)) #G i Joe!


#The same example as above, but using a dictionary instead of a mapping table
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict)) #G i Joe!

print("---------")

################################################################################
################################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# maketrans() method >>>>>>>>>>
# [[ Returns a translation table to be used in translations ]]
# Syntax:   str.maketrans(x, y, z)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.

# Parameter	Description
#   x	Required. If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
#   y	Optional. A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
#   z	Optional. A string describing which characters to remove from the original string.


#Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable)) #Hello Pam!
print("---------")

#Use a mapping table to replace many characters
txt = "Hi Sam!"
x = "mSa"
y = "eJo" ## has to be same number of chars like 'x'
mytable = str.maketrans(x, y)
print(txt.translate(mytable)) #Hi Joe!

#The third parameter in the mapping table describes characters that you want to remove from the string
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght" #which chars to remove?
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable)) #G i Joe!

#The maketrans() method itself returns a dictionary describing each replacement, in unicode
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z)) #{109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
mydict=str.maketrans(x, y, z)
print(txt.translate(mydict)) #G i Joe!
print("---------")

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# partition() & rpartition() method >>>>>>>>>>
# [[ Returns a tuple where the string is parted into three parts ]]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~ The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# ~ The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
#   ~ The first element contains the part before the specified string.
#   ~ The second element contains the specified string.
#   ~The third element contains the part after the string.

# partition() method searches for the first occurrence of the specified string.
# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string
# If the specified value is not found, the rpartition() method returns a tuple containing: 1 - an empty string, 2 - an empty string, 3 - the whole string


txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) #('I could eat ', 'bananas', ' all day')
x = txt.partition("apples")
print(x) #('I could eat bananas all day', '', '')   
print("---------")


txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x) #('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
x = txt.rpartition("apples")
print(x) #('', '', 'I could eat bananas all day, bananas are my favorite fruit')
print("---------")

################################################################################
################################################################################
################################################################################
################################################################################



