
thisdic = {
    "brand": "Ford",
    "Model": "Mustang",
    "Year": "1999"
    
}

x = thisdic.get("Model")
print(x)
x = thisdic.keys()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


x = car.keys()

print(x)

x = car.values()
print(x)

car ["color"] = "red"

print(x)

x = thisdic.items()

x = car.items()
print(x)

car["year"] = "2020" 
print(x)

if "model" in thisdic:
    print("yes, is one of the key dictonary")
    

thisdic["Year"] = "2025"    
print(x)

thisdic.update({"Year": 2025})
print(thisdic)
    
    