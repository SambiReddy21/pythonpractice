log_file = "logs.txt"

target_date = "2025-04-03"

with open("/home/chsambireddy/"+log_file, "r") as file:
    print("entered")
    for line in file:
        if line.startswith(target_date):
            print(line.strip())