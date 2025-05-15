numbers = [10, 5, 23, 89, 54, 21, 3]

largest_three = sorted(numbers, reverse=True)[:3]

print("Top 3 largest numbers: ", largest_three)
###########################################################

numbers = [10, 5, 23, 89, 54, 21, 3]

first = second = third = float('-inf')

for num in numbers:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num
        
print("Top 3 largest numbers:", first, second, third)