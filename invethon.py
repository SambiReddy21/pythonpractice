#1. Reverse string in python

text = "Helloworld"

reversed_text = text[::-1]
print(reversed_text)

def reverse_string(s):
    return s[::-1]

#text = input("Enter a string: ")
text1 = "shurthi"
print(f"reversed_string:", reverse_string(text1))

##################################

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
    
text = "pavanchandra"
print("reversed_string:", reverse_string(text))    

##############################################################################
#Find Max number in list and second max number in list
numbers = [2,3,4,5,66,77,88,99,110,1,0,4]

max_num = max(numbers)
numbers.remove(max_num)
second_max = max(numbers)

print("Max numer:", max_num)
print("Second max number:", second_max)

#######################################################
num1 = [7,14,17,18,212,3,4,5,9,11,23,44,55]

num1.sort(reverse=True)
second_largest = num1[1]

print("Second largest number:", second_largest)
first_largest = num1[0]
print("First_largest number:", first_largest)

#Remove vowels from a string

text = "Hello world"
vowels = "aeiouAEIOU"
no_vowel = "".join([char for char in text if char not in vowels ])

print(no_vowel)

res = ""
for char in text:
    if char in vowels:
       res = res + ""
    else:
        res = res + char
print(res) 

#############################################################3
import subprocess
import re

output = subprocess.check_output("ifconfig", text=True)

ip_addresses = re.findall(r"IPv4 Address[.\s]*: ([\d.]+)", output)
for ip in ip_addresses:
    print(ip)

#############################################################################
#Write a Python program to reverse those strings which contain no alphabets and others convert to uppercase.
data = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '#$%']

result = []

for item in data:
    if any(char.isalpha() for char in item):
        result.append(item.upper()) 
    else:
        result.append(item[::-1])
        
print(result)

#################################################################
#Write any string like “My name is XXXX” . Find the largest word in the string and print.
text = "my name is rajareddy22"
# Split the string into words

words = text.split() 
# Find the largest word using max with key=len

largest_word = max(words, key=len)

print("Largest word:", largest_word)

######################################################################################################
#Write  a program to find sum of all the numbers in a list?
numbers = [3,4,55,66,77,4,5,6,8]

total = sum(numbers)

print("Sum of all the numbers:", total)
########################################################################################################
#write a program to show all the number in descending order in list with out using inbuild functions
numbers = [5, 2, 9, 1, 7, 3]

for i in range(len(numbers)):
    max_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[max_index]:
            max_index = j
    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    
print("Numbers in descending order:", numbers)  #Descending order: [9, 7, 4, 2, 1]
####+++++++++++++++++++++++++++++++++    
numbers = [4,5,6,7,8,98]

n = len(numbers)
for i in range(n):
    for j in range(0, n - i -1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Descending order:", numbers)

#+++++++++++++++++++++++++++++++++++++++++++++++++
l1 = [45,12,89,2,6,5,78,3]

for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] > l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
            
print(l1)
print(l1[::-1])

######################################################################################
#write a pattern for ID address and find it is right or not
import re

def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'
    
    return bool(re.match(pattern, ip))

ip_addresses = "192.168.1.1"
if is_valid_ip(ip_addresses):
    print(f"{ip_addresses} is a valid IP addresses")
else:
    print(f"{ip_addresses} is a not valid ip addresses")
    
#########################################################################################
# # To validate the Maximum, minimum and average internet speed.
# import speedtest

# # Create a Speedtest object
# st = speedtest.Speedtest()

# # Download and upload speed in bits per second
# download_speed = st.download()
# upload_speed = st.upload()

# # Convert to Mbps (Megabits per second)
# download_mbps = download_speed / 1_000_000
# upload_mbps = upload_speed / 1_000_000

# # Calculate max, min, avg
# speeds = [download_mbps, upload_mbps]
# maximum = max(speeds)
# minimum = min(speeds)
# average = sum(speeds) / len(speeds)

# #display results

# print(f"Download Speed: {download_mbps:2f} Mbps")
# print(f"Upload Speed:   {upload_mbps:.2f} Mbps")
# print(f"Max Speed:      {maximum:.2f} Mbps")
# print(f"Min Speed:      {minimum:.2f} Mbps")
# print(f"Avg Speed:      {average:.2f} Mbps")

###########################################################################3
#From Product drop-down select MNO product options and get some text data from page

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time

# driver = webdriver.Chrome()

# driver.get("https://gmail.com")

# time.sleep(2)

# dropdown = Select(driver.find_element("id","productDropdown"))
# dropdown.select_by_visible_text("MNO")

# time.sleep(2)

# # Extract some text data from the page
# text_element = driver.find_element("id", "targetText")  # Replace with actual element ID or class
# print("Extracted text:", text_element.text)

# # Close browser
# driver.quit()

"""
 Key Notes:
Replace "productDropdown" and "targetText" with the actual HTML id, name, or xpath of the dropdown and data fields.

You can also use find_element_by_xpath() or find_element_by_css_selector() if IDs aren't available.

Add waits if the page dynamically loads content.

"""
#################################################################################################################################
# 25[0-5] matches 250 to 255

# 2[0-4][0-9] matches 200 to 249

# 1[0-9]{2} matches 100 to 199

# [1-9]?[0-9] matches 0 to 99 (handles leading digit correctly)

# \. is the dot separator

import re

def is_valid_ip(ip):
    # Regular expression pattern for IPv4
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}" \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    return re.match(pattern, ip) is not None

# Example usage
ip_address = "10.10.10.20"
if is_valid_ip(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is NOT a valid IPv4 address.")
    
######################################################################################
l1 = [113,34,44,55,6,7,8,9,11,22,33,44,100]

for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] > l1[j]:
            l1[j], l1[i] = l1[i],l1[j]
            
print(l1)
print(l1[-2])

##++++++++++++++++++++++++++++++++++++++
#----------------- Ip address extraction through Command prompt ----------------------
"""
25[0-5] matches 250 to 255

2[0-4][0-9] matches 200 to 249

1[0-9]{2} matches 100 to 199

[1-9]?[0-9] matches 0 to 99 (handles leading digit correctly)

\. is the dot separator

The entire match ensures 4 octets separated by dots

Test Examples:
✅ Matches: 192.168.0.1, 10.0.0.255, 255.255.255.255, 0.0.0.0

❌ Doesn’t match: 256.0.0.1, 192.168.0.999, 192.168.0, abc.def.ghi.jkl

"""

# Ip address extraction through Command prompt
import re
ip_addr = input("enter ip address: ")
match = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[0-5][0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[0-5][0-5])$",ip_addr)
print(match)
if match:
    print("It is a valid ip address")
else:
    print("Not a valid ip address")
	
 
 ##################################################################
#  import re

# def is_valid_ip(ip):
#     pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}" \
#               r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
#     return re.match(pattern, ip) is not None

# ip_address = "256.256.256.256"
# if is_valid_ip(ip_address):
#     print(f"{ip_address} is a valid IPv4 address.")
# else:
#     print(f"{ip_address} is an invalid IPv4 address.")
############################################################################################    
# ## r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}" \
# #               r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
#r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$
# 250-259 25[0-5]
# 200-249 2[0-4][0-9]
# 100-199 1[0-9]{2}
# 0-99 [1-9][0-9]
# {3}"\
#############################################3
import re
ip_addr = input("enter ip address: ")
pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}" \
          r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
match =re.match(pattern, ip_addr)
print(match)
if match:
    print("It is a valid ip address")
else:
    print("Not a valid ip address")
    
###########################################################################################################
#Write a Python program to find the length of a given list of non-empty strings.

words = ['cat', 'car', 'fear', 'center']

for word in words:
    print(len(word))
    print(words.count(word))
###########################################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

for i in num:
    print(num.count(i))
    

