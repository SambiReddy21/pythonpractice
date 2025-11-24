# Write a Python program to reverse those strings which contain no alphabets and others convert to uppercase.
# ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '#$%']

data = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '#$%']

result = []
for item in data:
    if any(char.isalpha() for char in item):
        result.append(item.upper())
    else:
        result.append(item[::-1])
print(result)