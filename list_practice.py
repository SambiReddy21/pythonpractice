#Lists (Dynamic Array)
#A list is an ordered, mutable collection of elements.

my_list = [1,2,3,4,5,6]

my_list.append(7)
print(my_list)

my_list.remove(3)
print(my_list)

my_list.insert(3, 3)
print(my_list)

my_list.insert(7, 8)
print(my_list)


#What is the difference between list.append() and list.extend()?

#append() adds a single element to the end of the list.
#extend() adds elements of another iterable (like another list) to the list.

#How do you remove duplicates from a list?

my_list1 = [1,2,3,4,3,2,4,5]

unique_list = list(set(my_list1))

print(unique_list)


#Tuples (Immutable Ordered Collection)
#A tuple is an immutable ordered collection of elements.

#Interview Questions:

#Why use a tuple instead of a list?
#Tuples are faster and use less memory since they are immutable.
#They can be used as dictionary keys.

#Can you modify a tuple?
#No, but you can create a new tuple by concatenating or slicing.

my_tuple = (1,2,4,5,6,7,8)
print(my_tuple[1])
print(my_tuple[3])
print(my_tuple[4])

"""

Sets (Unordered Collection of Unique Elements)
A set is an unordered collection that does not allow duplicate values.

"""

my_set = {1,2,3,4,5,6,4,3,2,1}

print(my_set)

my_set.add(7)
print(my_set)


#How do you find the intersection of two sets?

s1 = {1,2,3}
s2 = {1,2,4,5}

print(s1.intersection(s2))

print(s1.issubset(s2))
print(s1.issuperset(s2))


"""
List: Dynamic Array
What is the difference between list.append() and list.extend()?
Answer:

append(x) adds x as a single element to the end of the list.
extend(iterable) adds all elements of the iterable to the list.

"""


lst = [1,2,3]
lst.append([4,5])
print(lst)

lst1 = [1,2,3]
lst1.extend([4,5])
print(lst1)

lst1.reverse()
print(lst1)

lst2 = [1,2,3,4,5,6,7,8]
reve = lst2[::-1]
print(reve)

"""
Can you modify a tuple?
Answer: No, tuples are immutable. However, you can create a new tuple by concatenation.
"""

tup = (1,2,3,4,5)

tup1 = tup + (6,7,8)

print(tup1)


my_dict = {"name": "Raju", "age": 23}

for key, value in my_dict.items():
    print(key, "->", value)
    
#Q15: How do you reverse words in a sentence?

sentence = "Hello World"

reverse_sentence = " ".join(sentence.split()[::-1])

print(reverse_sentence)


reverse_sentence.split()

print(reverse_sentence)


#1. Find the First Non-Repeating Character in a String

from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)
    for char in s:
        if count [char] == 1:
            return char
    return None

print(first_non_repeating_char("leetcode"))
print(first_non_repeating_char("aabb"))
        
        
