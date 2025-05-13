"""
Print the Fibonacci sequence – Python
To print the Fibonacci sequence in Python, we need to generate a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The Fibonacci sequence follows a specific pattern that begins with 0 and 1, and every subsequent number is the sum of the two previous numbers.

Mathematically, the Fibonacci sequence can be represented as:

F(n) = F(n-1) + F(n-2)


Where:
F(0) = 0
F(1) = 1
F(n) for n > 1 is the sum of the two preceding numbers.


The sequence looks like this:


0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …

"""

n = 20
n1 = 0
n2 = 1

print("Fibonacci sequence: ")
print(n1)
print(n2)
sum = 0

while sum <= n:
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum
    
