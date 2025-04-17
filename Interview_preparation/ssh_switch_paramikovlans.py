import paramiko
import re

#switch credentials
host = "192.168.1.1"
username = "admin"
password = "password"
command = "show vlan brief"

#establish ssh connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)

#excute command

stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.read().decode()

#ssh close the ssh connection

ssh.close()

#extract vlan id using regex
vlans =re.findall(r"(\d+)\s+\S+", output)

#print the vlans
print("VLANS in the switch:", vlans)