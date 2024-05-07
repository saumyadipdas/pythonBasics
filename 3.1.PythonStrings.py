########################################

# Type Conversion

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("---------")


########################################

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("---------")

#Note: In the result, the line breaks are inserted at the same position as in the code.

########################################
########################################

### Strings are Arrays

#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1
#Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1]) #Get the character at position 1 (remember that the first character has the position 0)
print("---------")

########################################

# Looping Through a String
a="Hello World"
for x in a :
    print(x)
print("---------")

########################################

# String Length

a = "Hello, World!"
print(len(a))
print("---------")

########################################

# Check String

txt = "The best things in life are free!" #Check if "free" is present in the following text:
print("free" in txt)
print("---------")
txt="The best thing is life is free"
print("free" not in txt)
print("---------")

########################################

# IF condition

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print("---------")
if not "love" in txt:
  print("No, 'love' is not present.")
print("---------")

########################################

