import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print("您当前的主机名为" + hostname + "\n您当前的IP地址为" + ipaddr)