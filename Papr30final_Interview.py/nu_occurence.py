num = [4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]
result = {}

# for i in num:
#     if i not in result:     
#         result[i]= num.count(i)
#     #print((i, num.count(i)))
# print(result)
    
for i in num:
    if i not in result:
        result[i] = 1
    else:
        result[i] +=1
        
print(result)