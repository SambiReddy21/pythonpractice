"""
Lambda Functions in Python
A lambda function (also called an anonymous function) in Python is a small, single-expression function that does not require a name (def keyword). 
It is commonly used for short, simple operations where defining a full function is unnecessary.


"""
    
def add(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(add(5, 3))
print(add_lambda(5, 3))


#Using map() with Lambda

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]


#Using filter() with Lambda

nums = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print(even_numbers)  # Output: [2, 4, 6]



#Using reduce() with Lambda

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24


#Example 3: Sorting with Lambda

students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
sorted_students = sorted(students, key=lambda x: x[1])  # Sort by marks
print(sorted_students) # Output: [('Bob', 75), ('Charlie', 85), ('Alice', 90)]