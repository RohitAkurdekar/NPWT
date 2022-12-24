#!/usr/bin/python3

import paramiko
import getpass
import time

ip_add = input("please enter IP addr: ")

user_name = input("Enter device name: ")

password = getpass.getpass()

print("IP   : ",ip_add)
print("UNAME: ",user_name)
print("PASS : ",password)


ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_add,username=user_name,password=password)

send_ping = "ping -c 5 " + ip_add + " \n"
print("Successful connection")

rc=ssh_client.invoke_shell()
time.sleep(1)
rc.send(send_ping)
time.sleep(5)

rc.send("ifconfig\n")
time.sleep(1)

rc.send("mkdir ~/Desktop/demoProjectRohit\n")
time.sleep(1)

rc.send("cd ~/Desktop/demoProjectRohit/\n")
time.sleep(1)

rc.send("touch cipher.md")
time.sleep(5)

output = rc.recv(10000)

captured_output = output.decode('utf-8').split("\r\n")

for data in captured_output:
    print(data)
print("command successfull!!!")
ssh_client.close

'''

------------------ OUTPUT -------------------------------------------------------
iotdev$ ./RPI_Paramiko.py 
please enter IP addr: 192.168.77.185
Enter device name: diot
Password: 
IP   :  192.168.77.185
UNAME:  diot
PASS :  diot

#************************************************************************************

Successful connection

#************************************************************************************

Linux raspberrypi 5.15.61-v7+ #1579 SMP Fri Aug 26 11:10:59 BST 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.

Last login: Sat Dec  3 22:15:23 2022 from 192.168.77.76

#********************* PING ***********************************************************

diot@raspberrypi:~$ ping -c 5 192.168.77.185 

PING 192.168.77.185 (192.168.77.185) 56(84) bytes of data.
64 bytes from 192.168.77.185: icmp_seq=1 ttl=64 time=0.181 ms
64 bytes from 192.168.77.185: icmp_seq=2 ttl=64 time=0.170 ms
64 bytes from 192.168.77.185: icmp_seq=3 ttl=64 time=0.154 ms
64 bytes from 192.168.77.185: icmp_seq=4 ttl=64 time=0.176 ms
64 bytes from 192.168.77.185: icmp_seq=5 ttl=64 time=0.171 ms

--- 192.168.77.185 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4161ms
rtt min/avg/max/mdev = 0.154/0.170/0.181/0.009 ms

#****************** IFCONFIG **************************************************************

diot@raspberrypi:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.77.185  netmask 255.255.255.0  broadcast 192.168.77.255
        inet6 fe80::cc12:be67:3401:a794  prefixlen 64  scopeid 0x20<link>
        ether b8:27:eb:b9:a8:27  txqueuelen 1000  (Ethernet)
        RX packets 29466  bytes 28755898 (27.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9771  bytes 1055253 (1.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 129  bytes 12919 (12.6 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 129  bytes 12919 (12.6 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

#****************** MKDIR **************************************************************

diot@raspberrypi:~$ mkdir ~/Desktop/demoProjectRohit

diot@raspberrypi:~$ cd ~/Desktop/demoProjectRohit/

diot@raspberrypi:~/Desktop/demoProjectRohit$ touch cipher.md

#****************** CLOSE Connection and exit **************************************************************

command successfull!!!

#****************** EoC **************************************************************

'''
