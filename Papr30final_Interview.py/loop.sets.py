#you can loop through the set items by using a for loop.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
    print(len(x))
    
    """
    Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

Union
The union() method returns a new set with all items from both sets.
    
    """
set1 = {"a", "b", "c"}
set2= {1,2,3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2| set3| set4
print(myset)

z = set1.union(set2)
print(z)

set1.update(set2)
print(set1)

#Join set1 and set2, but keep only the duplicates:


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#Difference
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set3 = set1.difference(set2)

print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 -set2
print(set3)

"""
The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

Example
Use the difference_update() method to keep the items that are not present in both sets:
"""
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.


set1.difference_update(set2)
print(set1)

set3 = set1.symmetric_difference(set2)

print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set3 = set1 ^ set2
print(set3)

set11 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}

set11.symmetric_difference_update(set22)

print(set11)


"""
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others




"""