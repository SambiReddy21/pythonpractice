"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

"""

thisislist = ["banana", "cherry", "apple","mango"]

# print(thisislist)
# print(len(thisislist))

# for i in thisislist:
#     # print(len(thisislist))
#     print(thisislist.count(i))
    
words =  ["grape", "banana", "cherry", "apple","mango"]

for word in words:
    print(len(word))
    print(words.count(word)) 
    print(type(words))
    
    
'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


'''    
l1 =  ["grape", "banana", "cherry", "apple","mango"]
       
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[-1])
print(l1[-2])
print(l1[-3])
print(l1[-4]) 

word1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]       

for word in word1:
    print(len(word))

print(word1[1])
print(word1[2])
print(word1[3])
print(word1[-1])
print(word1[-2])
print(word1[-3])  
print(word1[0::5])
print(word1[-2::-3])
print(word1[-3::-4])  
    
