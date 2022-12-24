#!/usr/bin/python3
import getpass
import telnetlib
import time

ip_add = input("please enter IP addr: ")

user_name = input("Enter device name: ")

password = getpass.getpass()

print("IP   : ",ip_add)
print("UNAME: ",user_name)
print("PASS : ",password)

tn = telnetlib.Telnet(ip_add)
#tn.open(ip_add)

print("connecting.....")

tn.read_until(b"raspberrypi login: ")
tn.write(user_name.encode("ascii")+b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode("ascii")+b"\n")


send_ping = "ping -c 5 " + ip_add + " \n"

print("connection successfull")

tn.write(send_ping.encode("ascii"))

time.sleep(5)
tn.write(b"ifconfig\n")
time.sleep(2)
tn.write(b"touch filecdac.txt\n")
time.sleep(1)
tn.write(b"mkdir /home/diot1915/Desktop/demoProject_tel \n")
time.sleep(1)
tn.write(b"cd /home/diot1915/Desktop/demoProject_tel \n")
time.sleep(1)
tn.write(b"touch demoproject_tel.txt\n" )
tn.write(b"exit \n")
output = tn.read_all()

captured_output=output.decode('utf-8').split("\r\n")
for i in captured_output:
    print(i)

print("command successfull")
tn.close()



"""
------------------ OUTPUT -------------------------------------------------------

iotdev$ ./RPI_TELNET.py 

please enter IP addr: 192.168.77.200
Enter device name: diot1915
Password: 

IP   :  192.168.77.200
UNAME:  diot1915
PASS :  diot1915

connecting.....
connection successfull

ping -c 5 192.168.77.200 
Linux raspberrypi 5.15.76-v7+ #1597 SMP Fri Nov 4 12:13:17 GMT 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Dec 10 22:27:54 GMT 2022 from 192.168.77.205 on pts/2

diot1915@raspberrypi:~$ ping -c 5 192.168.77.200 

PING 192.168.77.200 (192.168.77.200) 56(84) bytes of data.
64 bytes from 192.168.77.200: icmp_seq=1 ttl=64 time=0.139 ms
64 bytes from 192.168.77.200: icmp_seq=2 ttl=64 time=0.164 ms
64 bytes from 192.168.77.200: icmp_seq=3 ttl=64 time=0.165 ms
64 bytes from 192.168.77.200: icmp_seq=4 ttl=64 time=0.159 ms
ifconfig
64 bytes from 192.168.77.200: icmp_seq=5 ttl=64 time=0.155 ms

--- 192.168.77.200 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4154ms
rtt min/avg/max/mdev = 0.139/0.156/0.165/0.009 ms

diot1915@raspberrypi:~$ ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.77.200  netmask 255.255.255.0  broadcast 192.168.77.255
        inet6 fe80::c968:de4a:d762:968d  prefixlen 64  scopeid 0x20<link>
        ether b8:27:eb:66:95:8b  txqueuelen 1000  (Ethernet)
        RX packets 22872  bytes 22941886 (21.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10911  bytes 1397824 (1.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 75  bytes 7995 (7.8 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 75  bytes 7995 (7.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether b8:27:eb:33:c0:de  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

diot1915@raspberrypi:~$ touch filecdac.txt
diot1915@raspberrypi:~$ mkdir /home/diot1915/Desktop/demoProject_tel 
mkdir: cannot create directory ‘/home/diot1915/Desktop/demoProject_tel’: File exists
diot1915@raspberrypi:~$ cd /home/diot1915/Desktop/demoProject_tel 
diot1915@raspberrypi:~/Desktop/demoProject_tel$ touch demoproject_tel.txt
exit 
diot1915@raspberrypi:~/Desktop/demoProject_tel$ exit 
logout

command successfull


"""
