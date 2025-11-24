#1.Write a program to print multiplication table of a given number using for loop.

# number = int(input("Enter the multiplication number: "))

# for i in range (1,11):
#     print(f"{number} X {i} = {number * i}")
    


#5.Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number to multiplication table in reverse order: "))

for i in range(10, 0, -1):
    print(f"{n} X {i} = {n * i}")
    

for i in range(5):
    if i == 2:
        continue
    print(i)
      
 
str = "Python"
reversed_str = ""
for char in str:
    reversed_str = char + reversed_str
print(reversed_str)


x = 5
while x > 0:
    print(x)
    x -= 1
    

for i in range(10):
    if i == 5:
        break
    print(i)
    
for i in range(5):
    if i == 2:
        continue
    print(i)
 
#Nested Loops (Multiplication Table)
#Q10: Write a program to print a multiplication table using nested loops   
    
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()