from netmiko import ConnectHandler
import time

router ={
        "device_type": "cisco_xe",
        "hostname": "192.168.1.1",
        "username": "admin",
        "password": "password",
        "secreat":"enable password", 
}

#functuon to get bgp summary
def get_bgp_summary(connection):
    connection.enable() # type: ignore
    output = connection.send_command("show ip bgp summary")
    return output
    
#step 1: Login and fetch bgp summary
print("Loggin into the router ...")
net_connect = ConnectHandler(**router)
bgp_before_reload = get_bgp_summary(net_connect)
print("BGP Summary (Before Reload):\n", bgp_before_reload)

#save the output to a file
with open("bgp_before.txt", "w") as file:
    file.write(bgp_before_reload)
    
#Step 2: Reload the router
print("Reloading the router...")
net_connect.send_command_timing("reload", strip_command=False)
net_connect.send_command_timing("\n", stri_command=False) #Confirm reload
net_connect.disconnect()

#step 3: wait for the router to to comeback online
print("Waiting for the router to reboot")
time.sleep(120)

#step 4: Login again and check bgp
print("Reconnecting to the router...")
net_connect = ConnectHandler(**router)
bgp_after_reload = get_bgp_summary(net_connect)
print("BGP Summary (After Reload):\n", bgp_after_reload)

#save teh new output

with open("bgp_after.txt", "w") as file:
    file.write(bgp_after_reload)
    
#Close the connection
net_connect.disconnect()

print("BGP status saved before and after reload.")