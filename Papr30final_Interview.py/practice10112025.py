import copy

#Shallow copy: Copies only references to nested objects.
#Deep copy: Copies all nested objects recursively.

a = [[1,2],[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)

print(b)
print(c)

####################################################################################
##factorial numbers
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#using a for loop
num = 6
fact = 1

for i in range(1, num + 1):
    fact *= i
    
print("factorial of", num, "is", fact)

"""num = 5          # The number for which we want to find the factorial
fact = 1         # Initialize factorial result to 1 because factorial multiplication starts with 1

for i in range(1, num + 1):  # Loop from 1 to 5 (inclusive)
    fact *= i               # Multiply the current factorial value by i and update fact

print("Factorial of", num, "is", fact)  # Output the factorial result

Explanation of the logic:
The factorial of a number 
n
n (denoted as 
n
!
n!) is the product of all positive integers from 1 to 
n
n.

Initialize the variable fact to 1 since multiplying by 1 does not change the value and it serves as the base for multiplication.

The for loop iterates from 1 to num (which is 5), multiplying fact with each value of i in each iteration.

After the loop, fact holds the value of 
5!=5×4×3×2×1=120
5!=5×4×3×2×1=120.

The print statement outputs the calculated factorial.

Factorial for 5 calculation in each iteration:
Iteration 1: fact = 1 * 1 = 1
Iteration 2: fact = 1 * 2 = 2
Iteration 3: fact = 2 * 3 = 6
Iteration 4: fact = 6 * 4 = 24
Iteration 5: fact = 24 * 5 = 120

So, the program prints:
Factorial of 5 is 120   """

###########################################################################################
l1 = [100, 99, 1, 1, 5, 8, 34, 34, 0, 22, 22]

res = []

for item in l1:
    if item not in res:
        res.append(item)
        
print(res) #removes the duplicate values
#################################################################################
l2 = [100, 99, 1, 1, 5,5, 8, 8, 34, 34, 0, 22, 22]

for i in l2:
    if l2.count (i) > 1:
        l2.remove (i)
    
print(l2)


################################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

result = {}

for i in num:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

print(result)

############################################################################################
    #In Python, a prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. This means it can only be divided evenly by 1 and the number itself. 
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
    print("not prime") 

#####################################################################################3
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  

for word in words:
    print(word)
    print(len(word))
#####################################################################################################
def reverse_string(s):
    reversed_string = " "
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
test = "hello pavan"
print("reversed_string", reverse_string(test))

############################################################

def reverse_string(s):
    return s [::-1]

test1 = "hello ramarao"

print("reversed_string", reverse_string(test1))

######################################################################################
#9. Python code for Fibonacci series

n = 10
n1 = 0
n2 = 1

print("fibronacci sequence: ")
print(n1)
print(n2)
sum = 0

while sum <= n:
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum
####################################################################################
l3 = [1,2,3,4,5,6,7,8,9,10,11,12]

res_list = []

for i in range(0,len(l3),2):
    res_list.append(l3[i:i+2])

print(res_list) #output [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
#############################################################################################
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("kiwi")
print(y)
thistuple = tuple(y)
print(thistuple) #output ('apple', 'banana', 'cherry', 'kiwi')

##################################################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    # print(word)
    # print(len(word))
    print(word, end=", ")


 ################################################################################################
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

###########################################################################################################

num = 121
reverse = int(str(num)[::-1])

if num == reverse:
    print("palindrome")
else:
    print("not palindrome")

# st1 = input("Enter a string: ")
# if(st1 == st1[::-1]):
#     print("This is a palindrome")
# else:
#     print("Not a palindrome")
    
    

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
################################################################3

# import calendar

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))

# cal = calendar.month(year, month)
# print(cal)

# ###########################################################################
# word = "121"
# rev = ""

# for ch in word:
#     rev = ch + rev

# if word == rev:
#     print("palindrome")
# else:
#     print("not a palindrome")
######################################################################################
x = 15

if x > 10:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

##############################################################
marks = 80

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("fail")

##################################################
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("invalid username or password")

###################################################
"""from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
import time


router = {
    "device_type": "cisco_xe",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "password",
    "secret": "enable password",
}

#show ip get bgp summary
def get_bgp_smmary(connection):
    connection.enable()
    output = connection.send_comamnd("show ip bgp summary")
    return output
try:
    
    # login and fetch bgp summary
    print("Logging into the router...")
    net_connect = ConnectHandler(**router)
    bgp_before_reload = get_bgp_summary(net_connect)
    print("BGP Summary (Before Reload):\n", bgp_before_reload)


    #save the output to a file

    with open("bgp_before.txt", "w") as file:
        file.write(bgp_before_reload)
	    
    #step2: Reload the router
    print("Reloading the router...")
    net_connect.send_command_timing("reload", strip_command=False)
    net_connect.send_command_timing("\n", strip_command=False) #Confirm reload
    net_connect.disconnect()


    #step 3: wait for the orouter to comeback online
    print("waiting for the router to reboot...")
    time.sleep(120) #adust based on router boot time


    #step 4: Login again and check BGP
    Print("Reconnecitng to the router...")
    net_connect = ConnectHandler(**router)
    bgp_after_reload = get_bgp_summary(net_connect)
    print("BGP Summary (After Reload):\n", bgp_after_reload)

    #save the new output
    with open("bgp_after.txt", "w") as file:
        file.write(bgp_after_reload)
    
    #close the connection
    net_connect.disconnect()


    print("BGP status saved before and after reload.")

except NetMikoTimeoutException:
    print("Connection Timeout: Device unreachable!")
except NetMikoAuthenticationException:
    print("Authentication Failed: Check username/password!")
except Exception as e:
    print(f"Unexpected Error: {e}")  """

###################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

res = {}

for i in num:
    if i not in res:
        res[i]= 1
    else:
        res[i] += 1
print(res) # {4: 2, 1: 2, 3: 6, 2: 1, 8: 1, 7: 1}

##################################################################################################
"""from netmiko import ConnectHandler
import time

router ={
        "device_type": "cisco_xe",
        "hostname": "192.168.1.1",
        "username": "admin",
        "password": "password",
        "secreat":"enable password", 
}

#functuon to get bgp summary
def get_bgp_summary(connection):
    connection.enable() # type: ignore
    output = connection.send_command("show ip bgp summary")
    return output
    
#step 1: Login and fetch bgp summary
print("Loggin into the router ...")
net_connect = ConnectHandler(**router)
bgp_before_reload = get_bgp_summary(net_connect)
print("BGP Summary (Before Reload):\n", bgp_before_reload)

#save the output to a file
with open("bgp_before.txt", "w") as file:
    file.write(bgp_before_reload)
    
#Step 2: Reload the router
print("Reloading the router...")
net_connect.send_command_timing("reload", strip_command=False)
net_connect.send_command_timing("\n", stri_command=False) #Confirm reload
net_connect.disconnect()

#step 3: wait for the router to to comeback online
print("Waiting for the router to reboot")
time.sleep(120)

#step 4: Login again and check bgp
print("Reconnecting to the router...")
net_connect = ConnectHandler(**router)
bgp_after_reload = get_bgp_summary(net_connect)
print("BGP Summary (After Reload):\n", bgp_after_reload)

#save teh new output

with open("bgp_after.txt", "w") as file:
    file.write(bgp_after_reload)
    
#Close the connection
net_connect.disconnect()

print("BGP status saved before and after reload.") """
################################################################################################

# with open("test11112025.txt") as file:
#     file.write

######################################################################
test4 = [1,2,3,4,5,5,6,6,4,3,2,2]
uniquie_test4 = list(set(test4))
print(uniquie_test4) # [1, 2, 3, 4, 5, 6]

############################################################
list4 = [1,2,3,4,5,5,6,6,4,3,2,2]

uniquie_list4 = []

for i in list4:
    if i not in uniquie_list4:
        uniquie_list4.append(i)
print(uniquie_list4)

###################################################################################
"""
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.3.1",
    "username": "admin",
    "password": "password",
    "secret": "secret password",
    
}

connection = ConnectHandler(**device)
connection.enable()

config_commands = [
    "interface loopback0",
    "ip address 10.1.1.1 255.255.255.0",
    "description Configured-by-Netmiko",
        
]

output = connection.send_config_set(config_commands)
print(output)

connection.send_command("write memory")

connection.disconnect()

"""
###########################################################################################################
logs = [
    {"level": "INFO", "message": "Interface up"},
    {"level": "WARNING", "message": "High CPU usage"},
    {"level": "ERROR", "message": "Link down on Gi0/1"},
    {"level": "INFO", "message": "New route added"},
    {"level": "CRITICAL", "message": "Device unreachable"}
]

for log in logs:
    print(f"[{log['level']}] {log['message']}")

#########################################################################################
logs = [
    {"level": "INFO", "message": "Interface up"},
    {"level": "ERROR", "message": "Link down"},
    {"level": "WARNING", "message": "Memory usage high"},
    {"level": "ERROR", "message": "BGP session down"},
]

for log in logs:
    if log["level"] == "ERROR":
        print("X",log["message"] )
###############################################################################################################
logs = [
    {"level": "INFO", "message": "Interface up"},
    {"level": "INFO", "message": "Route learned"},
    {"level": "ERROR", "message": "Interface down"},
    {"level": "WARNING", "message": "CPU high"},
    {"level": "ERROR", "message": "BGP neighbor lost"},
]

log_count = {}

for log in logs:
    level = log["level"]
    if level in log_count:
        log_count[level] += 1
    else:
        log_count[level] = 1

print(log_count)

#########################################################################################
num = 121

reverse = int(str(num)[::-1])

if num == reverse:
    print("palindrome")
else:
    print("not palindrome")
########################################

str = "racecar"
if (str==str[::-1]):
    print("palindrome")
else:
    print("not palindrome")
#############################
word = "kayak"
result = ""

for ch in word:
    result = ch + result
    
if word == result:
    print("palidrome")
else:
    print("not palidrome")
#################################################
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
"""from netmiko import ConnectHandler

device =[
    {"host": "10.1.1.1","device_type": "cisco_ios","username": "admin", "password":"cisco123"},
    {"host": "10.1.1.2","device_type": "cisco_ios","username": "admin", "password":"cisco123"}
]
    
for dev in device:
    try:
        conn = ConnectHandler(**dev)
        print(conn.sent_command("show version"))
        conn.disconnect()
    except Exception as e:
        print(f"Connection failed to {dev['host']}:{e}) """

############################################################################################
"""from netmiko import ConnectHandler

device = {
    "device_type":"cisco_ios",
    "host": "10.1.1.2",
    "username": "admin",
    "password": "cisco",
    "secret": "pass123"
}

connect = ConnectHandler(**device)
output = connect.send_command("show ip interface brief")
print(output)
connect.disconnect()"""
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

################################################################################
"""import requests 

resp = requests.get("https://api.github.com")
if resp.status_code == 200:
    print("Success")
else:
    print("Failed:", resp.status_code)"""
#################################################################################
x = 11
result = "Even" if x % 2 == 0 else "Odd"
print(result)
###################################################################################
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")

##############################################################################
for number in range(1, 20):
  if number % 2 == 0:
    print(f"even: {number}")
else:
   if number % 2 == 1:
     print(f"odd: {number}")
        
######################################################################################
#a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).

n = 7
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
##############################################################################################################
"""File handling in Python allows you to create, read, write, append, and delete files.

Python provides a built-in function:

open("filename", "mode")


Common modes:

Mode	Description
'r'	Read (default)
'w'	Write (overwrites existing file)
'a'	Append (adds to the end)
'x'	Create (fails if file exists)
'r+'	Read and Write
'w+'	Write and Read (overwrites file) """
###############################################################
file = open("sample11122025.txt", "w")
file.write("hello python")
file.write("hello world")
file.write("realme")

file.close
##########################################################
file = open("sample11122025.txt", "r")
content = file.read()
print(content)
file.close()
#########################################################
with open("sample11122025.txt", "r") as file:
    content = file.read()
    print(content)
    
##############################################################
numbers = [10, 50, 20, 70, 40]

# Find max number
max_num = max(numbers)

# Remove max and find second max
numbers.remove(max_num)
second_max = max(numbers)

print("Max number:", max_num)
print("Second max number:", second_max)

###########################################################################
text = "Hello World! Welcome to Python 3."
vowels = "aeiouAEIOU"
no_vowels = "".join([char for char in text if char not in vowels])
print(no_vowels)

###########################################################    #################################
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

for result in test_results.values():
    if result == "PASS":
        passed_testcases += 1
    elif result == "FAIL":
        failed_testcases += 1

print(f"Total Test Cases: {total_testcases}")
print(f"Passed Test Cases: {passed_testcases}")
print(f"Failed Test Cases: {failed_testcases}")

###############################################################################################
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

for keys in test_results.keys():
    print(f"Keys is: {keys}")
    if test_results[keys] == "PASS":
        passed_testcases += 1
    elif test_results[keys] == "FAIL":
        failed_testcases += 1
        
print(f"Total_testcases: {total_testcases}")
print(f"Passed_testcases: {passed_testcases}")
print(f"Failed_testcases: {failed_testcases}")  

#########################################################################################
devices = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]

for ip in devices:
    print(f"Connecting to device {ip}...")
    # Simulate command execution
    print(f"Running 'show version' on {ip}")
################################################################################
"""from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "10.1.1.1", "username": "admin", "password": "cisco"},
    {"device_type": "cisco_ios", "host": "10.1.1.2", "username": "admin", "password": "cisco"},
]

for device in devices:
    print(f"\nConnecting to {device['host']}...")
    connection = ConnectHandler(**device)
    output = connection.send_command("show ip interface brief")
    print(output)
    connection.disconnect() """

    #########################################################################################################
logs = [
    "INFO: Interface up",
    "ERROR: Link down on Gi0/1",
    "WARNING: High CPU usage",
    "ERROR: BGP neighbor lost"
]

for line in logs:
    if "ERROR" in line:
        print(line)    
        
#############################################################################################################
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

for keys in test_results.keys():
    if test_results[keys]=="PASS":
        passed_testcases += 1
    elif test_results[keys] == "FAIL":
        failed_testcases += 1
        
print(f"Total_testcases: {total_testcases}")
print(f"Passed_testcases: {passed_testcases}")
print(f"Failed_testcases: {failed_testcases}")

##############################################
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")
    
###############################
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
########################################################################
"""
You can create a Fibonacci series in Python using an iterative approach with a loop or a recursive approach with a function. The iterative method is more efficient for larger numbers, where you start with the first two numbers (\(0\) and \(1\)) and repeatedly calculate the next number by adding the previous two. The recursive method involves a function that calls itself,
but it can be less efficient for large sequences due to repeated calculations. 

"""
################################################################################
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=", ")
        a, b = b, a+b
        
print(fibonacci(10))
###############################################################################
def fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for i in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
        
print(fibonacci(10))
#############################################################################
logs = [
    {"level": "INFO", "message": "Interface up"},
    {"level": "INFO", "message": "Route learned"},
    {"level": "ERROR", "message": "Interface down"},
    {"level": "WARNING", "message": "CPU high"},
    {"level": "ERROR", "message": "BGP neighbor lost"},
]

log_count = {}

for log in logs:
    level = log["level"]
    if level in log_count:
        log_count[level] += 1
    else:
        log_count[level] = 1
        
print(log_count)
################################################################################################################################
logs = [
    {"level": "INFO", "message": "Interface up"},
    {"level": "ERROR", "message": "Link down"},
    {"level": "WARNING", "message": "Memory usage high"},
    {"level": "ERROR", "message": "BGP session down"},
]

for log in logs:
    if log["level"] == "ERROR":
        print("X", log["message"])
##############################################################################################################################
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] +=1
    else:
        count[fruit] = 1

print(count)
################################################################################################################################
students = {
    "101": {"name": "Ravi", "marks": 85},
    "102": {"name": "Priya", "marks": 92},
}

for roll, details in students.items():
    print("Roll No:", roll)
    for key, value in details.items():
        print("", key, ":", value)    
################################################################################################################################
numbers = [10, 5, 23, 89, 54, 21, 3]

largest_n1 = sorted(numbers, reverse=True)[:1]
print("Top 2 largest numbers:",largest_n1)

largest_two = sorted(numbers, reverse=True)[:2]
print("Top 2 largest numbers:",largest_two)

largest_three = sorted(numbers, reverse=True)[:3]
print("Top 3 largest numbers:",largest_three)

#######################################################################################################################

