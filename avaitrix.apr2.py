# n = 7
# res = 1
# i = 1

# while i <= n:
#     res = res * i
#     i = i + 1
# print(res)


# num = 1   
# while num <= 8:
#     print(num)
#     num += 1
    
    
num = 1
while num <= 10:
    if num == 9:
        break #skip the from 9
    print(num)
    num += 1

fruits = ["apple", "mango", "grapes", "chikku"]

for fruit in fruits:
    print(fruit)
    
 
    
    
for num in range(1, 10):
    print(num)
    

for num in range(1, 20):
    if num == 10:
        continue
    print(num)
    
    
for i in range(1,21):
      print(i)  
      
def is_leap(year):
    # leap = False
    
    # Write your logic here
    
    return(year % 4 == 0 and year %100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))
print(is_leap(year))



n = 5
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end= "")
    a, b = b,  a + b
    
