"""
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()
print(thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)

thislist.sort(reverse=True)
print(thislist)

"""
Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):
"""

def myfunc(n):
    return abs(n - 20)

thilist3 = [100,3,4,5,18,21,20,67,7,8,100]
thilist3.sort(key=myfunc)
print(thilist3)

thislist1.reverse()
print(thislist1)

thislist.reverse()
print(thislist)

thislist.sort(key=str.upper)
print(thislist)

newlist = thislist.copy()
print(newlist)

mylist = list(thislist)
print(mylist)

mylist = thislist[:]
print(mylist)