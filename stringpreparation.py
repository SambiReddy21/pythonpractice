#1. Convert a CamelCase string to snake_case (HelloPython)
# HelloPython should convert to _hello_python

cc1 = "_hello_Python"

res = ""
for ch in cc1:
    if ch.isupper():
        res += "_"+ch.lower()
    else:
        res += ch
print(res)


upp1 = "hello python"
print(upp1.upper())

low1 = "HELLO PYTHON"
print(low1.lower())


t1 = "hello python"
print(t1.title())

t2 = "hello python"
print(t2.capitalize())

# t3 = "hello python"

# for i in t3:
#     print(t3)
  
t4 = "Hello Python"  
print(t4.casefold())


test = "_HELLO _WORLD"

res1 = ""

for ch in test:
    if ch.isupper():
        res1 += "-"+ch.lower()
    else:
        res1 += ch
print(test)

print(len(test))

#2. Remove all occurrences of a specified character in a string

