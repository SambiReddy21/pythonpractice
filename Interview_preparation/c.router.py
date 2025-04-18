from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException, NetmikoTimeoutException

cisco_router = {
    "device_type": "cisco_ios",
    "host": "192.16.2.1",
    "username": "admin",
    "password": "password",
    "secret": "enable password",
     
}
try:
    connection = ConnectHandler(**cisco_router)
    connection.enable()
    output = connection.send_command("show ip int brief")
    print(output)
    connection.disconnect()
    
except NetmikoAuthenticationException:
    print("Authentication failed.check username/password/enable secret.")
except NetmikoTimeoutException:
    print("Connection time out. Device may be unreachable.")
except NetmikoTimeoutException:
    print(f"An unexpected error occurred: {e}")
        
