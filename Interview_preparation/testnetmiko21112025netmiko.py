########################################################################################################
"""1. What is Netmiko?

Answer:
Netmiko is a Python library built on top of Paramiko that simplifies SSH connections to network devices such as Cisco, Juniper, Arista, HP, and more. It allows engineers to automate device configuration, command execution, and network validation.

✅ Designed specifically for network automation
✅ Supports multi-vendor devices
✅ Easier than raw Paramiko

"""

########################################################################################################
# devices = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]

# for ip in devices:
#     print(f"Connecting to device {ip}...")
#     # Simulate command execution
#     print(f"Running 'show version' on {ip}")
################################################################################
"""from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "10.1.1.1", "username": "admin", "password": "cisco"},
    {"device_type": "cisco_ios", "host": "10.1.1.2", "username": "admin", "password": "cisco"},
]

for device in devices:
    print(f"\nConnecting to {device['host']}...")
    connection = ConnectHandler(**device)
    output = connection.send_command("show ip interface brief")
    print(output)
    connection.disconnect() """

#############################################################################################################

####################################################################
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
############################################################################################
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.3.2",
    "username": "admin",
    "password": "pass123",
    "enable_password": "secreat123"
    }


connections = ConnectHandler(**device)
output =connections.send_commands("show ip interface brief")
print(output)
connections.disconnect()

####################################################################################
#How do you push configuration using Netmiko?#
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.3.2",
    "username": "admin",
    "password": "pass123",
    "enable_password": "secreat123"
    }

config_commands = [
    "interface GigabitEthernet0/1",
    "description Configured via Netmiko",
    "no shutdown"

]
net_connect = ConnectHandler(**device)
net_connect.send.config_set(config_commands)
print(output)
connections.disconnect()

###########################################################################################################
#How do you handle multiple devices?
from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "10.1.1.1", "username": "admin", "password": "cisco"},
    {"device_type": "cisco_ios", "host": "10.1.1.2", "username": "admin", "password": "cisco"},
]

for device in devices:
    print(f"\nConnecting to {device['host']}...")
    connection = ConnectHandler(**device)
    output = connection.send_command("show ip interface brief")
    print(output)
    connection.disconnect()
"""
for ip in devices:
    device['host'] = ip
    net_conn = ConnectHandler(**device)
    print(net_conn.send_command("show version"))

"""
##############################################################################################################
# net_conn.save_config()
# or

# net_conn.send_command("write memory")

#######################################################
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

try:
    net_connect = ConnectHandler(**device)
except NetmikoTimeoutException:
    print("Connection timed out")
except NetmikoAuthenticationException:
    print("Authentication failed")

####################################################################################
output = net_conn.send_command("show run interface g0/1")
if "description" in output:
    print("Config Success")

################################################################################    
# How do you automate config backup using Netmiko?
backup = net_conn.send_command("show running-config")
with open("backup.txt", "w") as f:
    f.write(backup)

###########################################################################################3
#How do you check device status before configuration?
ping = net_conn.send_command("ping 8.8.8.8")

##########################################################################################
#Real Interview Question: How do you automate VLAN creation?
vlans = ['vlan 10', 'name HR', 'vlan 20', 'name IT']
net_conn.send_config_set(vlans)
#######################################################################################
# How do you detect device prompt?
prompt = net_conn.find_prompt()

#############################################################################
#How do you automate reboot process?
net_conn.send_command("reload", expect_string=r'confirm')
#####################################################################################
# You need to configure NTP on 50 routers.

# Solution Approach:

# Fetch device IPs

# Loop through IPs with Netmiko

# Apply configs:


ntp_config = [
    'ntp server 10.10.10.1',
    'ntp update-calendar'
]
net_conn.send_config_set(ntp_config)


######################################################################3
from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_ios", "host": "192.168.1.1", "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.1.2", "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.1.3", "username": "admin", "password": "cisco123"}
]

for device in devices:
    print(f"Connecting to {device['host']}")
    connection = ConnectHandler(**device)

    output = connection.send_command("show ip interface brief")
    print(output)

    connection.disconnect()
################################################################################################################
#Parallel Execution with Multithreading (High-Scale)

from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor

def connect_device(ip):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "cisco123"
    }
    conn = ConnectHandler(**device)
    output = conn.send_command("show version")
    conn.disconnect()
    return f"{ip} -> Done"

devices = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(connect_device, devices)

for result in results:
    print(result)

############################################################################################################3
from netmiko import ConnectHandler
#import netmiko NetmikoAuthenticationException import netmiko NetmikoTimeoutException
from concurrent.futures import ThreadPoolExecutor    

def connect_device(ip):
    device = {
        "device_type": "cisco_ios",
        "host": "172.16.2.3",
        "username": "admin",
        "password": "cisco123"
    }
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("show version")
        conn.disconnect()
        return f"{ip} -> Success"
    except NetmikoTimeoutException:
        return f"{ip} -> Timeout"
    except NetmikoAuthenticationException:
        return f"{ip} -> Auth Failed"       