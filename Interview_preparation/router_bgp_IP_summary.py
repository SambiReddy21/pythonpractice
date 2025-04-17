from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
import time


router = {
    "device_type": "cisco_xe",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "password",
    "secret": "enable password",
}

#show ip get bgp summary
def get_bgp_smmary(connection):
    connection.enable()
    output = connection.send_comamnd("show ip bgp summary")
    return output
try:
    
    # login and fetch bgp summary
    print("Logging into the router...")
    net_connect = ConnectHandler(**router)
    bgp_before_reload = get_bgp_summary(net_connect)
    print("BGP Summary (Before Reload):\n", bgp_before_reload)


    #save the output to a file

    with open("bgp_before.txt", "w") as file:
        file.write(bgp_before_reload)
	    
    #step2: Reload the router
    print("Reloading the router...")
    net_connect.send_command_timing("reload", strip_command=False)
    net_connect.send_command_timing("\n", strip_command=False) #Confirm reload
    net_connect.disconnect()


    #step 3: wait for the orouter to comeback online
    print("waiting for the router to reboot...")
    time.sleep(120) #adust based on router boot time


    #step 4: Login again and check BGP
    Print("Reconnecitng to the router...")
    net_connect = ConnectHandler(**router)
    bgp_after_reload = get_bgp_summary(net_connect)
    print("BGP Summary (After Reload):\n", bgp_after_reload)

    #save the new output
    with open("bgp_after.txt", "w") as file:
        file.write(bgp_after_reload)
    
    #close the connection
    net_connect.disconnect()


    print("BGP status saved before and after reload.")

except NetMikoTimeoutException:
    print("Connection Timeout: Device unreachable!")
except NetMikoAuthenticationException:
    print("Authentication Failed: Check username/password!")
except Exception as e:
    print(f"Unexpected Error: {e}")
