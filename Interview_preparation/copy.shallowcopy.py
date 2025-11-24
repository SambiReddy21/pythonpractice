"""

Shallow Copy: If you modify a mutable object within the shallow copied object, the change will reflect in the original object because they share the same reference.
Deep Copy: Modifications to mutable objects within the deep copied object do not affect the original object, as all objects are fully copied and independent.

Shallow Copy: Use copy.copy() to create a shallow copy.
Deep Copy: Use copy.deepcopy() to create a deep copy.

"""


from copy import deepcopy
l1 = [1,2,3,4,[5, 6, 7]]
      
templist1 = deepcopy(l1)
templist1[4][1] = 10
print("original", l1)
print('copied :',templist1)


import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modifying the copied object
shallow_copied[1][1] = 99
print("Shallow Copied:", shallow_copied)  # Output: Shallow Copied: [[99, 2, 3], [4, 5, 6]]




import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

# Modifying the copied object
deep_copied[0][0] = 99
print("Deep Copied:", deep_copied)  # Output: Deep Copied: [[99, 2, 3], [4, 5, 6]]




def greet(name):
    print(f"Hello, {name}!")

greet("Sambi")