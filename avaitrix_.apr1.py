#Number reverse and check is it palindrome or not

# def reverse_number(n):
#     return int(str(n)[::-1])

# def is_palindrome(n):
#     return n == reverse_number(n)

# num =int(input("Enter a number: "))

# reversed_number = reverse_number(num)

# if is_palindrome(num):
#     print(f"{num} is a palindrom.")
# else:
#     print(f"{num} is not is not palindrome. reversed number is {reverse_number}.")



l1 = [125,2,14,9,45,67,89,121,567]

for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] > l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
            
print(l1)
print(l1[::-1])
        

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

text = input("Enter a string: ")
print("Reversed_string", reverse_string(text))    