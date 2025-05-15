l1 = [100, 99, 1, 1, 5, 8, 34, 34, 0, 22, 22]

res = []

# for item in l1:
#     if item not in res:
#         res.append(item)
        
# print(res)

for n in l1:
    if l1.count(n) > 1:
        l1.remove(n)
        
print(l1)
        