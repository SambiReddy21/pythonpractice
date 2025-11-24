thisdict = {
    "brand": "tata",
    "model": "tataindico",
    "year": 1988
    
}

thisdict["color"]= "white"
thisdict["color"]= "red"
print(thisdict)

thisdict.update({"color": "blue"})
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

# del thisdict
# print(thisdict)

thisdict.clear()
print(thisdict)

thisdi1 = {
    "brand": "tata",
    "model": "tataindico",
    "year": 1988
    
}

for x in thisdi1.keys():
    print(x)
    
for x in thisdi1.values():
    print(x)
    
for x, y in thisdi1.items():
    print(x, y)
    
mydict =thisdi1.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

myfamily.update({
    "child4": {
        "name": "abhi",
        "year": 2021
    }
})

print(myfamily)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
    
}

print(myfamily)

print(myfamily["child1"]["name"])

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
        
        
"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


"""        