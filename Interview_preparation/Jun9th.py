n = 12
i = 1
count = 0

while i <= n:
    if n == 0 or n == 1:
        count = count + 1
    i = i + 1
    
if count == 2:
    print("prime")
else:
    print("not a prime number")
    
############################################################################

def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
        
text = "chandrapavan"
print("reversed_string:", reverse_string(text))
#######################################################################################
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n-1)
    
num = 5

print(f"factorial of {num} is {factorial(num)}")
##################################################################################
dupli1 = [100, 99, 1, 1, 5, 8,99,34, 34, 0, 22, 22,55,55,44,44,77,77]
res = []
for item in dupli1:
    if item not in res:
        res.append(item)
print(res) #[100, 99, 1, 5, 8, 34, 0, 22, 55, 44, 77]

#################################################################################
for n in dupli1:
    if dupli1.count (n) > 1:
        dupli1.remove(n)
print(dupli1) #[100, 1, 5, 8, 99, 34, 0, 22, 55, 44, 77]


####################################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7,6,6,5,8,5,2]
result = {}

for i in num:
    if i not in result:
        result [i] = 1
    else:
        result [i] += 1 
print(result) #{4: 2, 1: 2, 3: 6, 2: 2, 8: 2, 7: 1, 6: 2, 5: 2}

####################################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    print(len(word))
    print(word)
####################################################################################
def reverse_string(s):
    return s[::-1]

text = "samba"
print("reversed_string", reverse_string(text))
#################################################################################

for i in range(1,11):
    print(i)
#################################################################################
def reverse_string(s):
    return s[::-1]
    
text= "sirishasagar"

print("Reversed_string", reverse_string(text))
################################################################################
#9. Python code for Fibonacci series

n = 10
n1 = 0 
n2 = 1

print("Fibonacci sequence")
print(n1)
print(n2)
sum = 0

while sum <= n:
    sum = n1 + n2
    print(sum, end="")
    n1= n2
    n2 = sum   #Fibonacci sequence
#0
#1
#1235813
###################################################################################
l1 = [1,2,3,4,5,6,7,8,9,10]

res_list = []
    
for i in range (0, len(l1),2):
    res_list.append(l1[i:i+2])
print(res_list) #[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
####################################################################################

l1 = [1,2,3,4,5,6,7,8,9,10]

res_list = []
    
for i in range (0, len(l1),3):
    res_list.append(l1[i:i+3])
print(res_list) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
######################################################################################
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("kiwi")
print(y)  #['apple', 'banana', 'cherry', 'kiwi']
thistuple=tuple(y)
print(thistuple) # ('apple', 'banana', 'cherry', 'kiwi')
#####################################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

newword = []
for word in words:
    if 'a' in word:
        newword.append(word)
    
print(newword)  #['apple', 'banana', 'orange', 'mango']
####################################################################################

num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

res = {}

for i in num:
    if i not in res:
        res [i] = 1
    else:
        res [i] += 1
        
print(res) ###{4: 2, 1: 2, 3: 6, 2: 1, 8: 1, 7: 1}
#####################################################################################
    



    
    