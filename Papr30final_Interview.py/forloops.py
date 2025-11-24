"""
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

"""

fruits = ["apple", "grape", "banana", "kiwi"]

for fruit in fruits:
    print(fruit)
    
for x in "banana":
    print(x)    
    
    
for x in fruits:
    print(x)
    if x == "banana":
        break    
    print(x)
    
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


"""

for x in range(6):
    print(x)      
    
for x in range(2, 6):
    print(x)      
    
for x in range(2, 30, 3):
     print(x)   
     
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("Finally finished!")     
     
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
         
for x in range(6):
    if x == 3: continue
    print(x)
else:
    print("Finally finished!")         
         