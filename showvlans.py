from netmiko import ConnectHandler, NetMikoAuthenticationException, NetmikoTimeoutException
import sleep


router = {
    "device_type": "cisco_iosxe",
    "hostname": "192.168.1.1",
    "username": "admin",
    "password": "password",
    "secret": "enable password",
       
}

try:
    