x, y, z = "orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

x=y=z = "Organge"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#unpack a list

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"

print(x, y,z)

x = 5
y = 10

print(x + y)

"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

"""

y = "awesome"
def myfunc():
    print("Python is " + y)
    
myfunc

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()
print("Python is " + x)

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Example
If you use the global keyword, the variable belongs to the global scope: Also, use the global keyword if you want to change a global variable inside a function.


"""

# def mufunc():
#     global x
#     x = "awesome"
    
    
# myfunc()
# print("Python is " + x)


x = "awesome"

def myfunc():
    global x
    x = "fantaistic"    
    
myfunc()

print("python is" + x)