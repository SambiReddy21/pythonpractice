num = 121
reverse = int(str(num)[::-1])

if num == reverse:
    print("palindrome")
else:
    print("not palindrome")

st1 = input("Enter a string: ")
if(st1 == st1[::-1]):
    print("This is a palindrome")
else:
    print("Not a palindrome")
    
    

# num = 12234
# temp = num
# reverse = 0
# while temp > 0:
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10    
# if num == reverse:
#     print("palindrome")
# else: 
#     print("not palindrome") 


import calendar

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

cal = calendar.month(year, month)
print(cal)