#!/usr/bin/python3
#@coptright adham hasan 
import os
os.system('sudo pip install builtwith --upgrade')
os.system('sudo pip install python-whois --upgrade')
os.system('sudo pip install http.client')
os.system('pip install colorama')
os.system("pip3 install DateTime")
os.system("pip3 install bs4")
os.system('clear')
from bs4 import BeautifulSoup 
import builtwith
import whois 
import requests 
import http.client
import socket 
from colorama import Fore
import sys
import datetime
import subprocess
import re 
########################################################
print('''\
   ░██████╗░███████╗████████╗    ██╗ 
   ██╔════╝░██╔════╝╚══██╔══╝    ██║ 
   ██║░░██╗░█████╗░░░░░██║░░░    ██║
   ██║░░╚██╗██╔══╝░░░░░██║░░░    ██║
   ╚██████╔╝███████╗░░░██║░░░    ██║
   ░╚═════╝░╚══════╝░░░╚═╝░░░    ╚═╝''')
print (" 1) Website Ip \n 2) Website Id \n 3) Website Headers \n 4) Scan Ports \n 5) Website HTML \n 6) emails ")
num = int(input("choose what you need : "))

#######################################################
if num == 1 :
   ips=input("url:- http://")
   ip = socket.gethostbyname_ex(ips)
   print(ip)

########################################################
elif num == 2 :
   domain = input("domain: ")
   built= builtwith.parse(domain)
   info = whois.whois(domain)
   print (built)
   print (info)

########################################################
elif num == 3:  
  h= http.client.HTTPConnection(input("url: "))

  h.request("GET", "/")

  data= h.getresponse()
  print(data.headers)

########################################################
elif num == 4 :
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
elif num == 5 :
    urlh=input('Enter url :')
    req=requests.get(urlh).text
    soup=BeautifulSoup(req, 'html.parser')
    print(soup)
    t=input("Enter Tag Name :")
    for x in range(1,10):
     find=soup.find(t)
     print(find)
elif num == 6: 
    UrlMail=input('Enter url :')
    r=requests.get(UrlMail).text
    s=BeautifulSoup(r, 'html.parser')
    with open('mail.txt', 'w') as a:
      a.write(s)
    
reg =re.search("\S{1,}\@\S{1,}", s)
print reg.group()
print reg.span()
 
