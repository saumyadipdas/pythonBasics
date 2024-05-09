
## Python divides the operators in the following groups:
#  ~  Arithmetic operators
#  ~  Assignment operators
#  ~  Comparison operators
#  ~  Logical operators
#  ~  Identity operators
#  ~  Membership operators
#  ~  Bitwise operators

################################################################################
################################################################################
################################################################################
################################################################################

#  ~  Arithmetic operators >>>>>>>>

x = 2
y = 5
print(x % y) #3
print(x ** y) #32 ####same as 2*2*2*2*2 //(to get a to the power b)

x = 15
y = 2
print(x / y) #7.5
print(x // y) #7  ####The floor division // rounds the result down to the nearest whole number
print("---------")


################################################################################
################################################################################

#  ~  Assignment operators >>>>>>>>
"""
=	x = 5	        x = 5	
+=	x += 3	        x = x + 3	
-=	x -= 3	        x = x - 3	
*=	x *= 3	        x = x * 3	
/=	x /= 3	        x = x / 3	
%=	x %= 3	        x = x % 3	
//=	x //= 3	        x = x // 3	
**=	x **= 3	        x = x ** 3	
&=	x &= 3	        x = x & 3	
|=	x |= 3	        x = x | 3	
^=	x ^= 3	        x = x ^ 3	
>>=	x >>= 3	        x = x >> 3	
<<=	x <<= 3	        x = x << 3	
:=	print(x := 3)	x = 3
                        print(x)
"""

x = 5
x += 3
print(x) #8

x = 5
x//=3
print(x) #1

x = 5
x ^= 3
print(x) #6

x = 5
x >>= 3
print(x) #0

x = 5
x <<= 3
print(x) #40

print(x := 3) #3
print("---------")

################################################################################
################################################################################

#  ~  Comparison operators >>>>>>>>
"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""
print("---------")

################################################################################
################################################################################

#  ~  Logical operators >>>>>>>>
"""
and 	Returns True if both statements are true	                x < 5 and  x < 10	
or	Returns True if one of the statements is true	                x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not     (x < 5 and x < 10)
"""
x = 5
print(not(x > 3 and x < 10)) #False

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
print("---------")

################################################################################
################################################################################

#  ~  Identity operators >>>>>>>>

### In Python, is and is not are used to check if two values are located at the same memory location.

# ~~~ Identity operator (is) and the Equality operator (==): The == operator compares the value or equality of two objects,
# ~~~                   whereas the Python "is" operator checks whether two variables point to the same object in memory.

"""
is 	        Returns True if both variables are the same object	    x is y	
is not	        Returns True if both variables are not the same object	    x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # returns True because x is equal to y

print("---------")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) # returns False because z is the same object as x
print(x is not y) # returns True because x is not the same object as y, even if they have the same content
print(x != y)     # returns False because x is equal to y
print("---------")


a = 'hello world'
b = 'hello world'
print(a is b) # returns True
print("---------")

#If you define these lists independently of each other, then they’re stored at different memory addresses and behave independently
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #False
print(a==b) #True
print("---------")

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is y1)  # prints True
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False
print("---------")
################################################################################
################################################################################

#  ~  Membership operators >>>>>>>>
### Membership operators are used to test if a sequence is presented in an object
"""
in 	        Returns True if a sequence with the specified value is present in the object	        x in y	
not in	        Returns True if a sequence with the specified value is not present in the object	x not in y
"""
x = ["apple", "banana"]
print("banana" in x) # returns True because a sequence with the value "banana" is in the list


print("---------")

################################################################################
################################################################################

#  ~  Bitwise operators >>>>>>>>
### Bitwise operators are used to compare (binary) numbers
"""
& 	AND	                Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	OR	                Sets each bit to 1 if one of two bits is 1	                                                            x | y	
^	XOR	                Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
~	NOT	                Inverts all the bits	                                                                                    ~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                    x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
"""
print(8 >> 2) #2
print(3 << 2) #12
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print("---------")

################################################################################
################################################################################
################################################################################
################################################################################

#  ~  Operator Precedence >>>>>>
# Operator precedence describes the order in which operations are performed.

print("---------")



print("---------")

################################################################################
################################################################################

# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right
print(5 + 4 - 7 + 3) #5
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""

print((6 + 3) - (6 + 3)) #0
print(100 + 5 * 3) #115
print("---------") 
################################################################################
################################################################################
################################################################################
################################################################################
