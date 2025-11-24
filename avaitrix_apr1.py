""" 
Factorial of a program
Factorial of a program by using recursion
Number reverse and check is it palindrome or not
Check vowels present or not in string and replace witht he given letter
sort the list
find out max number 
find out minimum number
find our second largest number


Python2 and python3 differences
data types in python
what is exception handling how do you handle it
difference between list and tuple
get keys in dictionary and values in dictionary
dict1 = {"name: "Ram","fruits":['bananna','apple','orange']}
range and xrange difference
copy vs deepcopy
difference between pop and popitems

"""

#Factorial of a program

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# num =int(input("Enter a number: "))

# print(f"Factorial of {num} is {factorial(num)}")


"""
The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.

Factorial of a Number using Loop

"""

# num = int(input("Enter a number: "))

# factorial = 1

#check factorial is not defined for negative numbers

# if num < 0:
#     print("Sorry, factorial does not exist for negative number")
# elif num == 0:
#     print("The factorial 0 to 1")
# else:
#     for i in range (1,num + 1):
#         factorial = factorial*i
#     print(f"The factorial of",num,"is",factorial)
    
    
# def factorial_iterative(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
# num =int(input("Enter a number: "))
# print(f"The factorial of {num} is {factorial_iterative(num)}") 


#Factorial of a program by using recursion


# def factorial(n):
#     if n == 0 or  n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# num =int(input("Enter a number: "))
# # res = factorial(5)
# # print(res)

# if num < 0:
#     print("Factorial is not defined negative number: ")
# else:
#     print(f"Factorial of {num} is {factorial(num)}")
    
    
    
n = 6
res = 1
i = 1
 
while i <= n:
     res = res * i
     i = i + 1
     
print(res)   
    
    
