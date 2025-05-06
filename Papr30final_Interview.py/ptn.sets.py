"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

"""

myset = {"apple", "banana", "cherry"}

print(myset)

"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Duplicates Not Allowed
Sets cannot have two items with the same value.
False and 0 is considered the same value:

True and 1 is considered the same value:
"""

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print(type(thisset))


"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""

thisset = set(("apple", "banana","cherry"))
print(thisset)

for x in thisset:
    print(x)
    
print("banana" in thisset)    
print("banana" not in thisset)


thisset.add("orange")

print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)
print(len(thisset))
