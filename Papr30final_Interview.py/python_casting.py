"""
Python Casting
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""

print("Hello World")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

a = "Hello World!"

print(a)
print(len(a))
print(type(a))
print(a[:2:5])
print(a[1])

for x in "banana":
    print(x)
    
txt = "this loop is presnt in banana"    

if 'is' in txt:
    print(txt)
    
print("loop" in txt)    

txt = "The sun rise in the east"

print("dog" is not txt) 

