from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
import time


router = {
    "device_type": "cisco_xe",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "password",
    "secret": "enable paasword" 
}

#show bgp get summary

def bgp_get_summary(connection):
    connection.enable()
    output = connection.send_command("show ip bgp summary")
    return output
    
    
try: 
    #login to the device
    print("logging to the router")
    net_connect = ConnectHandler(**router)
    bgp_before_reload = bgp_get_summary(net_connect)
    print("BGP summary (before reload):\n", bgp_before_reload)
    
    #show output file
    with open("bgp_before.txt", "w") as file:
        file.write(bgp_before_reload)
        	
    #step 2 device reload
    
    print("reloading the router...")
    net_connect.send_command_timing("reload", strip_command=False)
    net_connect.send_command_timing("\n", strip_command=False) #confirm the load
    net_connect.disconnect()
    
    
    #wait for device to come up
    print("waiting for device to reboot..")
    time.sleep(120) #adjust the time as per device platform
    
    #step-4 for get bgp summary after reboot
    print("connecting to the router")
    net_connect = ConnectHandler(**router)
    bgp_after_reload = bgp_get_summary(net_connect)
    print("bgp summary (after reload):\n", bgp_after_reload)
    
    
    #show out file after reboot
    with open("bgp_after.txt", "w") as file:	
        file.write(bgp_after_reload)
        
    #close the connections:
    net_connect.disconnec()
    
    
    print("bgp status saved before and after reload.")     
    
except NetMikoTimeoutException:
    print("connection timeout: Device unreachble")
except NetMikoAuthenticationException:
    print("Authentication Failed: check username/password!")     
except Exception as e:
    print(f"unexpected Error: {e}")
        
        