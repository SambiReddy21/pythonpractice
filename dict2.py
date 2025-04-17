"""
dictionary in Python?

Answer: A dictionary is an unordered collection of key-value pairs where keys must be unique and immutable (strings, numbers, tuples), but values can be any data type


"""

my_dict = {"name": "Alice","age": 45, "city":"bangalore"}
print(my_dict["name"])
print(my_dict.get("age"))

if "name" in my_dict:
    print("key exists")
    
for key, value in my_dict.items():
    print(key, ":", value)
    
    
dict2 = {"a": 1, "b": 2}
dict3 = {"c": 3, "d": 4}

merge_dict = {**dict2, **dict3}

print(merge_dict)

#print(my_dict["salary"])
print(my_dict.get("salary"))    


squares = {x: x**2 for x in range(10)}
print(squares)


scores = {"Alice":90, "charna":98, "aparna": 99}
max_key = max(scores, key=scores.get)
print(max_key)

#factorial 

res = 1
l1 = [res := res * i for i in range(1,11)]
print(l1)