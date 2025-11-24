from netmiko import ConnectHandler
import re

switch = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "password",
    "secret": "enable_password",
     
}

    #connect
try: 
    net_connect = ConnectHandler(**switch)
    net_connect.enable()

    #Run the command to get vlan infromation

    output = net_connect.send_command("show vlan breif")   
    
   #close the connection
    net_connect.disconnect()
    
    #Extract vlans IDS using regex
    
    vlans = re.findall(r"(\d+)\s+\S+", output)
    
    #print the vlans list
    print("VLANS in the switch:", vlans)

except Exception as e:
    print("Error:", str(e))
    
    
     
