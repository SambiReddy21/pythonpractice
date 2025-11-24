from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.3.1",
    "username": "admin",
    "password": "password",
    "secret": "secret password",
    
}

connection = ConnectHandler(**device)
connection.enable()

config_commands = [
    "interface loopback0",
    "ip address 10.1.1.1 255.255.255.0",
    "description Configured-by-Netmiko",
        
]

output = connection.send_config_set(config_commands)
print(output)

connection.send_command("write memory")

connection.disconnect()