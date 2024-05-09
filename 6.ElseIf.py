"""
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
Other programming languages often use curly-brackets for this purpose.
"""

################################################################################
################################################################################

a=33
b=23
if a>b :
    print("a>b")
elif a==b:
    print("a==b")
else:
    print("b>a")

print("---------")


################################################################################
################################################################################

## Short Hand If  >>>>>>
# ~ If you have only one statement to execute, you can put it on the same line as the if statement.
a = 2
b = 330
print("A") if a > b else print("B")
print("---------")

##One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print("---------")



################################################################################
################################################################################
################################################################################
################################################################################

### The pass Statement >>>>>>>>
#~  If statements cannot be empty, but if you for some reason have an if statement with no content,
#~      put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
print("---------")


################################################################################
################################################################################
################################################################################
################################################################################
