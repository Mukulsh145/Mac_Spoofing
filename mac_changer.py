# mac changer

import subprocess

print("select option")
print("1 : eth0")
print("2 : wlan0")

x = input("enter interface you want to change 1 or 2 :")

y = input("enter your mac :")

subprocess.run("sudo ifconfig" , shell=True)
subprocess.run("sudo ifconfig " + x + " down" , shell=True)
subprocess.run("sudo ifconfig " + x + " hw ether " + y , shell=True)
subprocess.run("sudo ifconfig " + x +" up" , shell=True)

print("your mac_address successfully changed")