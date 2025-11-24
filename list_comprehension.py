# print([n for n in range(1,21)])


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")
    
    
# num1 = int(input("Enter a number: "))
    
tables = [f"{i} X {j} = {i * j}" for i in range(1,21) for j in range(1,11)]
#print(tables, end= "") 
for item in tables:
    print(item)   



# even = [n for n in range(1, 21) if n % 2 == 0]
# print(even)

# odd = [n for n in range(1, 21) if n % 2 == 1]
# print(odd)


a = 10
b = 12

if a > b:
    print("a is greater than b")
else:
    print("a is less than b")
    

# def reverse_string(s):
#     return s[::-1]

# text = input("Enter a string: ")
# print(f"reversed_string:", reverse_string(text))

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
    
text= input("Enter a string: ")
print("Reversed_string:", reverse_string(text))