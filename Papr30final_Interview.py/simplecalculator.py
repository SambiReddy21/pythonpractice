def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divided by zero"
    return x / y

print("select operation:")
print("1. Add")
print("2. subtract")
print("3, mulitiplicaiton")
print("4. divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))

if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("Result:", multiplication(num1, num2))
elif choice == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")
    

    