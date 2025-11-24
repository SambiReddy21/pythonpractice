# numbers = [1,2,5,7,8,9,11,12,44,0]

# min_values = min(numbers)
# max_values = max(numbers)

# print("minimum values:",min_values)
# print("maximum values:", max_values)



# numbers = [2,3,4,5,6,9,11,23,45,67,100,0]

# min_values = numbers[0]
# max_values = numbers[0]

# for num in numbers:
#     if num < min_values:
#         min_values = num
#     if num > max_values:
#         max_values = num
        
# print("minimum_valves:", min_values)
# print("maxmum-values:", max_values)


num1 = [7,14,17,18,212,3,4,5,9,11,23,44,55]

num1.sort(reverse=True)
second_largest = num1[1]

print("Second largest number:", second_largest)


#Method 2: Using a Loop (Efficient Approach)

l1 = [2,3,4,5,94,11,23,44,55, 988]

first = second = l1[0]

for i in range(len(l1)):
    if l1[i] > first:
        first, second = l1[i], first
    elif l1[i] > second and l1[i] != first:
        second = l1[i]
print(first)
print(second)


s1 = [7,14,17,18,212,3,4,5,9,11,23,44,55]

s1.sort(reverse=True)
print(s1)


s2 = [7,14,17,18,212,3,4,5,9,11,23,44,55]

s2.sort()
print(s2)



