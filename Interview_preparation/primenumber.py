"""
What is a Prime Number?
A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

Examples of Prime Numbers:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...

Properties of Prime Numbers:
✔ 2 is the only even prime number (All other even numbers are divisible by 2).
✔ 1 is not a prime number (Prime numbers must have exactly two factors).
✔ Prime numbers have no divisors other than 1 and themselves.

"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")
    
    
    
n = 11    
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1
    
if count == 2:
    print("prime")
else:
    print("not a prime")