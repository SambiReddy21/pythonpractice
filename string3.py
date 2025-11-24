#Check if a given substring exists within a string.

test = "Python Testing is a testing"

test1 = "Test"

# if test1 in test:
#     print(f"substring found")
# else:
#     print(f"substring not found")
    
res = test.find(test1)
print(res)

if res == -1:
    print("not found")
else:
    print("found")
    
    
test2 = "Python testing is testing method"   
target = "t"
count = 0
for chr in test2:
    if chr == target:
        count += 1
print(count)
    
count = test2.count("o")
print(count)

"""
Using count(): This is ideal for counting a single character quickly and easily.
Using Loop: This method provides more control over counting process and allows for additional logic during counting.
Using collections.Counter: This is best option for efficiently counting all characters in a string with clear and concise code.

"""

from collections import Counter

s = "GeeksforGeeks"
count = Counter(s)
print(count["e"])


    