import csv
from netmiko import ConnectHandler

"""
device_type,host,username,password
cisco_ios,192.168.1.1,admin,admin
cisco_ios,192.168.1.2,admin,admin
cisco_ios,192.168.1.3,admin,admin
cisco_ios,192.168.1.4,admin,admin

"""

csv_file_path = "/home/chsambireddy/Desktop/devices.csv"

with open(csv_file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        device = {
            "device_type": row["device_type"],
            "host": row["host"],
            "username": row["username"],
            "password": row["password"]
        }
        try:
            conn = ConnectHandler(**device)
            print(f"\nConnected to {device['host']}")
            output = conn.send_command("show ip int brief")
            print(output)
            conn.disconnect()
        except Exception as e:
            print(f"Failed to connect to {device['host']}: {e}")
