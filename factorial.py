def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a number: "))
print(f"factorial of {num} is {factorial(num)}")

n = 11
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1
    
if count == 2:  
    
    print("prime number")
else:
    print("not a prime number")
    
 #######################################################################################################
    
    