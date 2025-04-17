# squares = [x ** 2 for x in range (10)]
# print(squares)

# even_numbers = [x for x in range(14)if x % 2 ==0]
# print(even_numbers)


# odd_numbers = [x for x in range(14)if x % 2 ==1]
# print(odd_numbers)


# words = ["hello", "world", "python"]
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)


# words1 = ["hello", "world", "python"]
# titlecase_words = [word.title() for word in words1]
# print(titlecase_words)


# #print evennumbers


# print(*[x for x in range(1, 21)])
# print([x for x in range(1, 21)])

# #prime number

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))

# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


#Here’s a Python program to reverse a string in different ways:

# def reverse_string(s):
#     return s[::-1]

# string = input("Enter a string: ")
# print("Reversed_string:", reverse_string(string))

# #Method 1: Using Slicing
# def reverse_string(s):
#     return s[::-1]

# string = input("Enter a string: ")
# print("reversed_string:", reverse_string(string))


# #Method 2: Using reversed() and join()

# def reverse_string(s):
#     return ''.join(reversed(s))


# string = input("Enter a string: ")
# print("Reversed_string:", reverse_string(string))



#Method 3: Using a Loop

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

string = input("Enter a string: ")
print("reveresed_string", reverse_string(string))



x = 10
if x > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5")