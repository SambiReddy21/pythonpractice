n = 12
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1
    
if count == 2:
    print("prime number")
else:
    print("not a prime")
    
###########################################################################
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = 5
print(f"factorial of {num} is {factorial(num)}")
############################################################################

for i in range(1,3):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
##############################################################################

num = 1
n = 10

while num <= n:
    print(num)
    num += 1
##############################################################################    

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
text = input("Enter a string: ")
print("reversed_string", reverse_string(text))

####################################################################################

text = "hello python"

reverse_string = text[::-1]
print(reverse_string)

############################################################################
text = "hello python"
vowels = "aeiouAEIOU"

no_vowels = "".join([char for char in text if char not in vowels])

print(no_vowels)    

#############################################################################
data = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '#$%']
result = []

for item in data:
    if any(char.isalpha() for char in item):
        result.append(item.upper())
    else:
        result.append(item[::-1])
print(result)

###################################################################################

words = ["cat", "mat", "fear", "center", "largetest"]

for word in words:
    print(len(word))
    
 ####################################################
num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]
 
result = {} 
 
for i in num:
    if i not in result:
         result[i] = 1
    else:
         result[i] += 1
print(result)  

###############################################
def is_leaf(year):
    return(year %4 == 0 and year %100 !=0) or (year % 400 == 0)

year = int(input("Enter a year: "))
print(is_leaf(year))
##############################################################
l1 = [2,3,4,5,94,11,23,44,55, 988]

first = second = l1[0]

for i in range(len(l1)):
    if l1[i] > first:
        first, second = l1[i], first
    elif l1[i] > second and l1[i] !=first:
        second = l1[i]
        
print(first)
print(second)
    