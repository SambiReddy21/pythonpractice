"""

Data Types in Python
Python has several built-in data types that categorize the different kinds of values a variable can store. The primary data types in Python are:

1. Numeric Types
int (Integer): Whole numbers, e.g., 10, -5, 0
float (Floating-point number): Numbers with decimals, e.g., 3.14, -0.5, 2.0
complex (Complex numbers): Numbers with real and imaginary parts, e.g., 2 + 3j

"""


a = 10

b = 3.45

c = 2 + 3j

print(type(a))
print(type(b))
print(type(c))



"""

2. Sequence Types
str (String): Ordered sequence of characters, e.g., "Hello", 'Python'
list (List): Ordered, mutable collection of items, e.g., [1, 2, 3, "Python"]
tuple (Tuple): Ordered, immutable collection of items, e.g., (1, 2, 3, "Python")
range (Range): Represents a sequence of numbers, e.g., range(1, 10)

"""


s = "python"
l = [1,2,3,4,5,6]
t = (1,2,3,4,5)
r = range(5)

print(type(s))
print(type(l))
print(type(t))
print(list(r))


"""
3. Set Types
set (Set): Unordered collection of unique elements, e.g., {1, 2, 3, 4}
frozenset (Immutable Set): Immutable version of a set, e.g., frozenset({1, 2, 3})

"""
s = {1,2,3,4,5}

fs = frozenset  ({1,2,3})

print(s)
print(type(s))
print(fs)
print(type(fs))

"""
4. Mapping Type
dict (Dictionary): Key-value pairs, e.g., {"name": "John", "age": 25}

"""

d = {"name": "Raju", "age": 30}

print(type(d))
print(d["name"])


"""
5. Boolean Type
bool (Boolean): Represents True or False
"""

x = True

y = False

print(x)

print(10<5)


"""
6. Binary Types
bytes: Immutable sequence of bytes, e.g., b'Python'
bytearray: Mutable sequence of bytes
memoryview: View of a bytes-like object

"""

b = b"Python"
ba = bytearray([65,67,68])

mv = memoryview(b)

print(type(b))
print(type(ba))
print(type(mv))


"""
Type Conversion
Python allows converting one data type into another using type conversion functions like int(), float(), str(), list(), etc.

"""

x = "100"
y = int(x)  # Converts string to integer
print(y, type(y))  # Output: 100 <class 'int'>

f1 = 55
f2 = float(f1)  # Converts int to float
print(f2, type(f2)) # Output: 10.0 <class 'float'>

c = [1,2,3,4,5,66] # Converts list to tuple
d = tuple(c)  

print(d, type(d))  # Output: (1, 2, 3) <class 'tuple'>



"""
1. What are the basic data types in Python?
Answer: The basic data types in Python are:

Numeric types: int, float, complex
Sequence types: str, list, tuple, range
Set types: set, frozenset
Mapping type: dict
Boolean type: bool
Binary types: bytes, bytearray, memoryview


"""

'''
. What is the difference between list and tuple?
Feature	                    List	               Tuple
Mutability	Mutable (can be modified)    	Immutable (cannot be modified)
Syntax	list = [1, 2, 3]                   	tuple = (1, 2, 3)
Performance	        Slower                      	Faster
Memory Usage      	Higher	                        Lower

'''

#How is a set different from a list?
#Answer:
#A set is unordered and does not allow duplicate values.
#A list is ordered and allows duplicates.

my_list = [1,2,2,3,3,4,4,5,6]

my_set = {1,2,3,4,3,2,4}

print(my_list)
print(my_set)

#What is the difference between deep copy and shallow copy?
#Answer:
#Shallow Copy: Copies the reference of the object, changes reflect in both.
#Deep Copy: Creates a completely new object, changes do not affect the original.

import copy

list1 = [[1,2,3,4], [5,6,7,8]]

copy_shallow = copy.copy(list1)
copy_deepcopy = copy. deepcopy(list1)

copy_shallow[0][0] = 99
print(list1)

copy_deepcopy[0][0] = 50
print(list1)


#6. What happens when you add an integer and a string?
#Answer: Python raises a TypeError because it does not allow implicit conversion.

a = 10
b = "20"

#print(a + b) #  TypeError: unsupported operand type(s) for +: 'int' and 'str'
   
print(a + int(b))

"""
What is the difference between mutable and immutable data types?
Mutable	Immutable
Can be modified after creation	                                 Cannot be modified after creation
list, dict, set, bytearray                                       int, float, str, tuple, frozenset

"""

