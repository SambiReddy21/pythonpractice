from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username":"admin",
    "password":"password",
    "secret":"secret password",
    
}

try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_command("show ip interface breif")
    print(output)
    net_connect.disconnect()
except Exception as e:
    print(f"Error connecting to device: {e}")
    