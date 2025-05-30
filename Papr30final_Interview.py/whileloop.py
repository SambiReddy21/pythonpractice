"""
Python Loops
Python has two primitive loop commands:

while loops
for loops
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

With the break statement we can stop the loop even if the while condition is true:


"""

i = 1
while i < 6:
     print(i)
     i += 1
     
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1
     
# With the continue statement we can stop the current iteration, and continue with the next:

#Continue to the next iteration if i is 3: 

     
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
         
         


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")         