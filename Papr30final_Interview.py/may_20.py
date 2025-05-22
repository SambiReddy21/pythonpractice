l1 = [100, 99, 1, 1, 5, 8, 34, 34, 0, 22, 22]

res = []

for item in l1:
    if item not in res:
        res.append(item)
        
print(res) #removed duplicate values in the list [100, 99, 1, 5, 8, 34, 0, 22]

################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]
result = {}

for i in num:
    if i not in result:
        result[i] = 1
    else:
        result[i] +=1
print(result)  #output {4: 2, 1: 2, 3: 6, 2: 1, 8: 1, 7: 1}

############################################################################
for n in l1:
    if l1.count(n) > 1:
        l1.remove(n)
print(l1)  #[100, 99, 1, 5, 8, 34, 0, 22]
################################################################################
def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorial (n-1)
num = 5

print(f"factorial of {num} is {factorial (num)}") #factorial of 5 is 120


#####################################################################
#Prime numbers are numbers that have only 2 factors: 1 and themselves. For example, the first 5 prime numbers are 2, 3, 5, 7, and 11. 
n = 12
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
###################################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    print(len(word))
###############################################################33
#Python code to reverse a string

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
        
text = "narendramodi"
print("reversed_string:", reverse_string(text)) #output reversed_string: idomardneran
##############################################################################

def reverse_string(s):
    return s[::-1]
    
text = "Lokambika"
print("reversed_string:", reverse_string(text))
##############################################################
#9. Python code for Fibonacci series
n = 20
n1 = 0
n2 = 1

print("Fibonacci sequence: ")
print(n1)
print(n2)
sum = 0

while sum <= n:
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum
    
##################################################################################
n = 12
i = 1
count = 0

while i <=n:
    if n % i == 0:
        count = count + 1
    i = i + 1
    
if count == 2:
    print("prime")
else:
    print("not prime") 
    
#################################################################################
l1 = [1,2,3,4,5,6,7,8,9,10]

res_list = []

for i in range(0, len(l1),2):
    res_list.append(l1[i:i+2])
    
print(res_list) #output [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

######################################################################################
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("kiwi")
print(y)
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'kiwi')
######################################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

# for word in words:
#     print(len(word))
#     # print(word)
#     # print(word,end="")
    
i = 0 
while i < len(words):
    print(words[i])
    i = i + 1
    
[print(x) for x in words]

#####################################################################################
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist) #['apple', 'banana', 'orange', 'mango']
####################################################################################
str1 = "This is testing"
output = str1.replace("testing", "testing"[::-1])
print(output)  #This is gnitset
######################################################

word1 = "comma"
word2 = "fizzy"

combined = word1 + word2

from collections import Counter
result = any(count > 1 for count in Counter (combined).values())
print(result)

#################################################################################################
import re

test_str = '<b>Hi</b> Hello <b>Best</b>. I love <b>Reading</b> from book.'

matches = re.findall(r'<b>(.*?)</b>', test_str)
print(" ".join(matches))  # Output: Hi Best Reading
