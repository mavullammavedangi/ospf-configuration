from netmiko import ConnectHandler

device={
"device_type" : "cisco_ios",
"host" : "192.168.237.161",
"username" : "vasu",
"password" : "Cisco123",
"secret" : "Cisco123"}

connection=ConnectHandler(**device)
connection.enable()
k=connection.find_prompt()
print(k)
output=connection.send_command("sh running-config | section ospf")
print(output)
connection.disconnect()