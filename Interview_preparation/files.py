"""
💡 Summary of with open Modes
Mode	Description
"r"	Read (File must exist)
"w"	Write (Overwrites existing file)
"a"	Append (Adds new content to the file)
"r+"	Read & Write (File must exist, does not overwrite)
"w+"	Write & Read (Overwrites the file)

"""


f = open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile.txt", "w")
f.write("this is sirisha \n this is sagar \n")
f = open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()


# try:
#     f = open("demofile.txt")  # Opens the file in read mode
#     print(f.read())  # Reads and prints file content
#     f.close()  # Closes the file
# except FileNotFoundError:
#     print("File not found. Please check the file name.")


f1 = open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile1.txt", "w")
l1 = ["this is hyderabad \n", "This is temple \n"]
f1.writelines(l1)
f1 = open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile1.txt", "r")
print(f1.readlines())
f.close()

with open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile1.txt", "r") as f:
    content = f.read()
    print(content)

with open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile1.txt", "w") as f:
    f.write("this is sagar!\n")
    f.write("this is mostly overwrite!\n")

with open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile1.txt", "r") as f:
    content = f.read()
    print(content)
with open("/home/chsambireddy/gitpython/pythonpractice/Interview_preparation/demofile.txt", "r") as f:  
    for line in f:
        print(line.strip()) T