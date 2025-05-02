"""
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
"""

fruits = ("apple", "banana", "cherry")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

"""
Loop Through a Tuple
You can loop through the tuple items by using a for loop.

"""

for fruit in fruits:
    print(fruit)
for fruit in range(len(fruits)):
    print(fruit)
    
    
i = 0 

while i < len(fruits):
    print(fruits[i])
    i = i + 1
        
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found