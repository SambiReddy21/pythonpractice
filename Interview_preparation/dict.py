"""
What is the difference between append() and extend() in Python?

Answer: append() adds a single element (including a list as a single item) to the list, while extend() merges another list's elements into the current list.

"""

l1 = [1,2,3]
l1.append([4,5,6])
print(l1)

l2 = [1,2,3,4]

l2.extend([5,6,7,8,9])
print(l2)

#What happens when we use append() with a string?
l3 = [1,2,3]
l3.append('abc')
print(l3)

l4 =[1,2,3,4]
l4.extend('abc')
print(l4)


a = [1,2,3]
b = [4,5]

a.append(b)
print(a)

a = [1,2,3,4]
b = {5,6}
a.extend(b)
print(a)