from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "192.168.1.1", "username": "admin", "password": "admin"},
    {"device_type": "cisco_ios", "host": "192.168.1.2", "username": "admin", "password": "admin"},
    {"device_type": "cisco_ios", "host": "192.168.1.3", "username": "admin", "password": "admin"},
    {"device_type": "cisco_ios", "host": "192.168.1.4", "username": "admin", "password": "admin"},
]

for device in devices:
    try:
        connection = ConnectHandler(**device)
        config = connection.send_command("show running-config")
        with open(f"{device['host']}_backup.txt", "w") as f:
            f.write(config)
        print(f"Back up completed for {device['host']}")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['host']} {e}")        
