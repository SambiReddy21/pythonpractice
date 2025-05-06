"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.



"""

thisdic = {
    "brand": "Ford",
    "Model": "Mustang",
    "Year": "1999"
    
}

print(thisdic)
print(len(thisdic))
print(type(thisdic))

for i in thisdic:
    print(i)

thisdic1 = dict(name ="John", age= 36,  country = "Norway")    
print(thisdic1)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""
