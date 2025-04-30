#a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).

n = 16
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count += 1
    i += 1
    
if count == 2:
    print("prime number")
else:
    print("not a prime number")
    
#factorial number 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
       return n * factorial(n -1)

n = int(input("Enter a number: "))
   
print(f"factorial of {n} is {factorial(n)}")


n = 5
fact = 1

for i in range(1, n+1):
    fact = fact * i
    
print("The factorial of 5 is :", end ="")
print(fact)

import math

print("the factorial of 5 is :", end="")
print(math.factorial(5))

