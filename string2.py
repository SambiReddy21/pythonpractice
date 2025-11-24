#2. Remove all occurrences of a specified character in a string
test = "Hello World"
rc = "l"
res = ""
for ch in test:    
    if ch == rc:
        res += ""
    else:
        res += ch
        
print(res)


occ = "Happy is man"
rc1 = "a"
res = ""
for ch in occ:
    if ch ==rc1:
        res += ""
    else:
        res += ch
print(res)

print(dir(str))