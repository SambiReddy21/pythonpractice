my_list = [1,2,3,4]
print("before modification", my_list)

my_list.append(5)
print("after modification", my_list)


name = "Sambi"
print("before modification", name)

name += " Reddy"    
print("after modification", name)

my_dict = {"name": "Sambi", "age": 44}

my_dict["age"] = 45
print(my_dict)


# my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 6

# print(my_tuple)

import time

current_time = time.time()
print(current_time)
#print(f"current time(seconds since epoch): {current_time}")

import datetime

current_time1 = datetime.datetime.now()
print(f"Current date and time: {current_time1}")