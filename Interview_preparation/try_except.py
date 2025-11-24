"""
Purpose:
The try block contains code that might raise an exception.

The except block catches and handles the exception if it occurs.

This prevents abrupt termination and allows alternative actions or logging.

"""

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("result:", result)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divided by zero!")
except Exception as e:
    print("An unexpected error occurred")
    
#greatest number

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third  number: "))
num4 = float(input("Enter the fourth number: "))

greatest_number = max(num1, num2, num3, num4) 

print(f"The greatest number is: {greatest_number}" )   