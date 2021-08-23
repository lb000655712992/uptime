#!/usr/bin/env python
import paramiko
from datetime import datetime


def uptime(username, password, IP, port):
    port = int(port)

    # Connect to Server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('show system uptime')
    result = stdout.read().decode()
    #print(str(result))
    str2 = str(result).split('\n')
    #print(str2)

    for i in str2:
        #print(i)
        str3 = i.split(' ')
        #print(str3[0])
        if str3[0] == "System":
            uptime = datetime.strptime(str3[2]+" "+str3[3], "%Y-%m-%d %H:%M:%S")
            print((datetime.now() - uptime))
            print((datetime.now() - uptime).seconds)
            return str(int((datetime.now() - uptime).seconds))