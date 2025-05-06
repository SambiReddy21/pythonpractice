"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.


"""
a = 33
b = 200
if b > a :
    print("b is greater than a")

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
    
a = 200
b = 33

if b > a :
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
    
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")
    
    
if a > b or a > c:
     print("At least one of the conditions is True")
     
 
a = 33
b = 200
 
if not a > b:
    print("a is NOT greater than b")
     
if b > a:
    pass            
        