import numbers


fruits = ["apple", "mango", "banana", "cherry", "fig"]

print(fruits)

print(fruits[0])
print(fruits[-1])
print(fruits[2])
print(fruits[-4])

fruits[0] = "straberry"
print(fruits)

fruits[-1] = "apple"
print(fruits)

fruits.append("elderberry")
print(fruits)

fruits.insert(2, "grape")
print(fruits)

fruits.remove("cherry")
print(fruits)

removed = fruits.pop(1)
print(f"removed:{removed}")

print(fruits)

if "apple" in fruits:
    print("apple in the list!")
    
for fruit in fruits:
    print(fruit, end="  ")
    
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruits}")
    
    
#even number  Filter even numbers from a list

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

#Create a new list with squares of numbers

squares = [n ** 2 for n in numbers]
print(squares)


triples = [n ** 3 for n in numbers]
print(triples)


fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)

index = fruits.index("apple")
print(f"Index of the apple: {index}")


#occurence count for an element

numbers = [1,3,2,3,4,3,2,5,6,7,8,9,10]

print(numbers.count(3))


new_list = fruits.copy()
print(new_list)

import copy
new_list1= copy.copy(fruits)
print(new_list1)