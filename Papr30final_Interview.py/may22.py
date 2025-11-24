lcom = [x for x in range(10) if x%2 if x%3] 

print(lcom)

n = 3
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
    
#######################################################################
def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
    
text="chandra"
print("reversed_string:", reverse_string(text))
##############################################################################
def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
        
num = 5
print(f"factorial of {num} is {factorial(num)}")
#####################################################################################
l1 = [100, 99, 1, 1, 5, 8, 34, 34, 0, 22, 22,55,55,44,44,77,77]

res = []

for item in l1:
    if item not in res:
        res.append(item)
    
print(res)
###################################################################
for n in l1:
    if l1.count (n) > 1:
        l1.remove(n)
        
print(l1)
######################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7,6,6,5,5]
result = {}

for i in num:
    if i not in result:
        result [i] = 1
    else:
        result[i] += 1
print(result)
#######################################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    print(len(word))
    #print(word)
###################################################################################
def reverse_string(s):
    return s[::-1]
text = "sirisha"

print("Reversed_string:", reverse_string(text))
###################################################################################
#9. Python code for Fibonacci series

n = 10
n1 = 0
n2 = 1

print("Fibonacci_sequence")
print(n1)
print(n2)
sum = 0

while sum <= n:
    sum = n1 + n2
    print(sum)
    n1=n2
    n2 = sum
######################################################################################
l1 = [1,2,3,4,5,6,7,8,9,10]

res_list = []

for i in range(0, len(l1),2):
    res_list.append(l1[i:i+2])
print(res_list)
#################################################################################
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("kiwi")
#print(y)
thistuple=tuple(y)
print(thistuple)

####################################################################################

words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

newlist = []

for word in words:
    if "a" in word:
        newlist.append(word)

print(newlist)
######################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

res = {}

for i in num:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1
     
print(res)
#################################################################    
from collections import Counter

num1 = [8,4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 7,3, 8, 7]

resu = Counter(num1)
print(resu)
