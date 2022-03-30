import os
import paramiko
import pathlib

def SendSSH(ip):
    os.system("ssh pi@" +str(ip))
