"""
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

"""
x = ("apple", "mango", "grape", "pomgrantie")

y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

y = list(x)
y.append("orange")
x = tuple(y)

print(x)

y = ("orange", )
x += y

print(x)
