fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] +=1
    else:
        count[fruit] = 1

print(count)

#############################################################
students = {
    "101": {"name": "Ravi", "marks": 85},
    "102": {"name": "Priya", "marks": 92},
}

for roll, details in students.items():
    print("Roll No:", roll)
    for key, value in details.items():
        print("", key, ":", value)    

################################################################################################################
logs = [
    "INFO: Interface up",
    "ERROR: Link down on Gi0/1",
    "WARNING: High CPU usage",
    "ERROR: BGP neighbor lost"
]

for line in logs:
    if "ERROR" in line:
        print(line)    

#############################################################################################################
logs = [
    {"level": "INFO", "message": "Interface up"},
    {"level": "INFO", "message": "Route learned"},
    {"level": "ERROR", "message": "Interface down"},
    {"level": "WARNING", "message": "CPU high"},
    {"level": "ERROR", "message": "BGP neighbor lost"},
]

log_count = {}

for log in logs:
    level = log["level"]
    if level in log_count:
        log_count[level] += 1
    else:
        log_count[level] = 1
        
print(log_count)
############################################################################################        