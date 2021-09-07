#!/usr/bin/python3
import os
os.system('sudo pip install builtwith --upgrade')

os.system('sudo pip install python-whois --upgrade')
os.system('sudo pip install http.client')
os.system('pip install colorama')
os.system('clear')
import builtwith
import whois 
import requests 
import http.client
import socket 
from colorama import Fore
import sys
import datetime
import subprocess
########################################################
print('''\
   ░██████╗░███████╗████████╗    ██╗ 
   ██╔════╝░██╔════╝╚══██╔══╝    ██║ 
   ██║░░██╗░█████╗░░░░░██║░░░    ██║
   ██║░░╚██╗██╔══╝░░░░░██║░░░    ██║
   ╚██████╔╝███████╗░░░██║░░░    ██║
   ░╚═════╝░╚══════╝░░░╚═╝░░░    ╚═╝''')
print (" 1) Website Ip \n 2) Website Id \n 3) Website Headers \n 4) Scan Ports ")
num = int(input("choose what you need : "))

#######################################################
if num == 1 :
   os.system('clear')
   ips=input("url: ")
   ip = socket.gethostbyname_ex(ips)
   print(ip)

########################################################
elif num == 2 :
   os.system('clear')
   url = input("url: ")
   built= builtwith.parse(url)
   info = whois.whois(url)
   print(built)
   print(info)

########################################################
elif num == 3:  
   os.system('clear')
  h= http.client.HTTPConnection(input("url: "))
  h.request("GET", "/")

  data= h.getresponse()
  print(data.headers)

########################################################
elif num == 4 :
   os.system('clear')
    remoteServer    = input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)

    print ("-" * 60)
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("-" * 60)

    try:
        for port in range(1,10025):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

    print ('Scanning Completed ')    
