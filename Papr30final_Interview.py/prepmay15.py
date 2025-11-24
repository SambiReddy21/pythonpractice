l1 = [100, 99, 1, 1, 5, 8, 34, 34, 0, 22, 22]

res = []

for item in l1:
    if item not in res:
        res.append(item)
        
print(res)
        

for n in l1:
    if l1.count(n) > 1:
        l1.remove(n)
        
print(l1)


#Python code for printing HelloWorld

print("Hello World")

#Python code to add two or more numbers
a = 10
b = 15

c = a + b

print(c)
####################################################
#Python code to find factorial of a number 

def factorial(n):
   if n == 0 or n ==1:
       return 1
   else:
       return n * factorial (n-1)
   
num = 5   
print(f"factorial of {num} is {factorial(num)}")

#############################################################

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))

################################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

result = {}

for i in num:
    if i not in result:
        result[i] = 1
    else:
        result[i] +=1
        
print(result)
###################################################################
words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    

for word in words:
    print(len(word))
#######################################################################
#Python code to reverse a string

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

text = "rajumba"
print("reversed_string:", reverse_string(text))
########################################################

def reverse_string(s):
    return s[::-1]

text = "lokambika"
print("reversed_string:", reverse_string(text))
###########################################################    
    

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
    
#Python code to check prime number

n = 13
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
    
##################################################################################################    
l1 = [1,2,3,4,5,6,7,8,9,10]
res_list = []
for i in range(0,len(l1),3):
    res_list.append(l1[i:i+3])
print(res_list)      # output [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

#####################################################################################################
l1 = [1,2,3,4,5,6,7,8,9,10]
res_list = []
for i in range(0,len(l1),2):
    res_list.append(l1[i:i+2])
print(res_list)    #output [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

####################################################################################################
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#print(y)
print(thistuple)