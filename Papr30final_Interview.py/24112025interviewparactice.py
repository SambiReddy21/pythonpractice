# factorial The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 (denoted as 5!) is 5 × 4 × 3 × 2 × 1 = 120. In Python, we can calculate the factorial of a number using various methods, such as loops, recursion, built-in functions
###############################################################
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
num1 = 5    
print(factorial(num1)) #120
#####################################################################
#factorial in loop
num  = 5
fact = 1

for i in range(1, num+1):
    fact *= i

print("factorial of", num, "is", fact) #factorial of 5 is 120
###############################################################
def fact(n):
    
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * fact(n - 1) 

# Driver Code
num = 5
print(fact(num))
         
############################################################
#reverse string
def reverse_string(s):
    return s[::-1]
text = "hello python"
print("Reversed_string:", reverse_string(text)) #Reversed_string: nohtyp olleh

####################################################################3
#reverse_num

def reverse_num(n):
    return int(str(n) [::-1])

num1 = 123

print("reverse_num: ", reverse_num(num1)) #reverse_num:  321

#######################################################
#removes the duplcate values in list
l1 = [100,22, 100,5,99,0, 99, 1, 1, 5, 8, 34, 34, 0, 22, 22]

res = []

for item in l1:
    if item not in res:
        res.append(item)
print(res) #[100, 22, 5, 99, 0, 1, 8, 34]

####################################################################

#count the duplicate values 
l2 = [100, 99, 1, 1, 5,5, 8, 8, 34, 34, 0, 22, 22]

for i in l2:
    if l2.count(i) > 1:
        l2.remove(i)
        
print(l2) #[100, 99, 1, 5, 8, 34, 0, 22]
#####################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

res = {}

for i in num:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1
        
print(res) #{4: 2, 1: 2, 3: 6, 2: 1, 8: 1, 7: 1}
######################################################################
#In Python, a prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. This means it can only be divided evenly by 1 and the number itself. 
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
    print("not prime number")
###################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  

for word in words:
    print(word)
    print(len(word))
    
###########################################################
def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

text = "hello pavan"

print("reversed_string", reverse_string(text)) #reversed_string navap olleh
#################################################
l3 = [1,2,3,4,5,6,7,8,9,10,11,12]

res_list = []

for i in range(0, len(l3), 2):
    res_list.append(l3[i:i+2])
    
print(res_list) #[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
#########################################################
thistuple = ("apple", "banana", "cherry")
y =list(thistuple)
y.append("kiwi")
print(y)
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'kiwi')


#########################################
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple) #(1, 2, 3)
#########################################
my_tuple = (1,2,3,4,5,6,7,8,9)
my_list = list(my_tuple)
print(my_list)
#########################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    # print(word)
    # print(len(word))
    print(word, end=", ") #apple, banana, cherry, orange, kiwi, melon, mango, 
###############################################################
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

result = []
for x in fruits:
    if  "a" in x:
        result.append(x)
    
print(result) #['apple', 'banana', 'orange', 'mango']
########################################################
num = 121
reverse = int(str(num)[::-1])

if num == reverse:
    print("palindrome")
else:
    print("not palindrome") #palindrome


########################################################

st1 = "madam"
if(st1 == st1[::-1]):
    print("palindrome")
else:
    print("not palindrome") #palindrome
########################################################

word = "kayak"
rev = ""

for ch in word:
    rev = ch + rev
if word == rev:
    print("palindrome")
else:
    print("not palindrome")
###################################################################

x = 15

if x > 25:
    print("x is greater than 25")
else:
    print("x is not greater than 25")
##################################################

marks = 95

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    
################################################################
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("login sucessfully")
else:
    print("password sucessfully")
###################################################################
a = "Hello World"

print(a.lower())
print(a.upper())
print(a.split(","))

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1,2,3]

for x in list2:
    list1.append(x)
    
print(list1)


word = "123"

result = ""

for ch in word:
    result = ch + result
    
if word == result:
    print("palindrome")
else:
    print("not palindrome")
    
####################################
def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))
##############################################

#############################################################
add = lambda x, y : x + y
print (add(2,3))

################################################
newlist = []

for x in fruits:
    if "a" in x:
      newlist.append(x)
        
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
print(newlist1)
print(newlist)

newlist = [x for x in range(1,11)]
newlist5 = [x for x in range(11) if x < 9]
print(newlist)
print(newlist5)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  

######################################################################################
# """table = [f"{x} x {j} = {x * j}" for x in range(1,21) for j in range(1,11)]

# for item in table:
#     print(item)"""
########################################################################
#fibonacci series up to terms

n  = 10
a, b = 0, 1

print("fibonacci series")
for i in range(n):
    print(a, end =" ")
    a, b = b, a + b
##########################################################3
# import requests 

# resp = requests.get("https://api.github.com")
# if resp.status_code == 200:
#     print("Success")
# else:
#     print("Failed:", resp.status_code)    
#################################################################
x = 21

result = "Even" if x % 2 == 0 else  "odd"

print(result)
##########################################################################
for x in range(1,11):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
#################################################################
for number in range(1, 20):
  if number % 2 == 0:
    print(f"even: {number}")
else:
   if number % 2 == 1:
     print(f"odd: {number}")

##############################################################
numbers = [10, 50, 20, 70, 40]

# Find max number
max_num = max(numbers)

# Remove max and find second max
numbers.remove(max_num)
second_max = max(numbers)

print("Max number:", max_num)
print("Second max number:", second_max)
#################################################################################
text = "Hello World! Welcome to Python 3."
vowels = "AEIOUaeiou"

no_vowels = " ".join ([char for char in text if char not in vowels])
print(no_vowels)

################################################################################################################
test_results = {
    "Login Test": "PASS",
    "Signup Test": "PASS",
    "Profile Update Test": "PASS",
    "Password Reset Test": "PASS",
    "Logout Test": "FAIL"
}

total_testcases = len(test_results)
passed_testcases = 0
failed_testcases = 0

for results in test_results.values():
    if results == "PASS":
        passed_testcases += 1
    elif results == "FAIL":
        failed_testcases += 1

print(f"Total testcases: {total_testcases}")
print(f"Passed testcases: {passed_testcases}")
print(f"Failed testcases: {failed_testcases}")
##############################################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
        
print("Even_numbers",even_numbers)
print("Odd_numbers", odd_numbers)

#############################################################
for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

#############################################################################################
# numbers = [10, 5, 23, 89, 54, 21, 3]

largest_n1 = sorted(numbers, reverse=True)[:1]
print("Top 2 largest numbers:",largest_n1)

largest_two = sorted(numbers, reverse=True)[:2]
print("Top 2 largest numbers:",largest_two)

largest_three = sorted(numbers, reverse=True)[:3]
print("Top 3 largest numbers:",largest_three)

###############################################################################################################

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

def connect_device(ip):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "cisco123"
    }
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show version")
        conn.disconnect()
        return f"{ip} -> Success"
    except NetmikoTimeoutException:
        return f"{ip} -> Timeout"
    except NetmikoAuthenticationException:
        return f"{ip} -> Auth Failed"                       

        

      