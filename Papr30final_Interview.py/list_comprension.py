"""
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

"""

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

newlist = []

for x in fruits:
    if "a" in x:
      newlist.append(x)
        
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
print(newlist1)
print(newlist)

newlist = [x for x in range(1,11)]
newlist5 = [x for x in range(11) if x < 9]
print(newlist)
print(newlist5)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  

table = [f"{x} x {j} = {x * j}" for x in range(1,21) for j in range(1,11)]

for item in table:
    print(item)
    
    