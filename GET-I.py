#!/usr/bin/python3
# @copyright adhamhas

import os
import sys
import socket
import requests
import http.client
import subprocess
import re
import datetime
from bs4 import BeautifulSoup
import builtwith
import whois
from colorama import Fore, Style

# Initial setup
os.system('clear')
print(Fore.GREEN + '''
   ░██████╗░███████╗████████╗    ██╗ 
   ██╔════╝░██╔════╝╚══██╔══╝    ██║ 
   ██║░░██╗░█████╗░░░░░██║░░░    ██║
   ██║░░╚██╗██╔══╝░░░░░██║░░░    ██║
   ╚██████╔╝███████╗░░░██║░░░    ██║
   ░╚═════╝░╚══════╝░░░╚═╝░░░    ╚═╝
''' + Style.RESET_ALL)

print(Fore.CYAN + '''
1) Website IP
2) Website Technologies & Whois Info
3) Website Headers
4) Port Scanner
5) Website HTML and Tag Search
6) Extract Emails from Website
7) Extract Phone Numbers from Website
''' + Style.RESET_ALL)

try:
    num = int(input(Fore.YELLOW + "Choose what you need: " + Style.RESET_ALL))
except:
    print("Invalid number.")
    sys.exit(1)

########################################################
if num == 1:
    target = input("Enter domain (without http://): ")
    try:
        ip = socket.gethostbyname_ex(target)
        print("IP Addresses:", ip)
    except Exception as e:
        print("Error:", e)

########################################################
elif num == 2:
    domain = input("Enter domain (without http://): ")
    try:
        built = builtwith.parse(domain)
        info = whois.whois(domain)
        print(Fore.GREEN + "\nTechnologies:" + Style.RESET_ALL, built)
        print(Fore.GREEN + "\nWhois Info:" + Style.RESET_ALL)
        print(info)
    except Exception as e:
        print("Error:", e)

########################################################
elif num == 3:
    host = input("Enter domain (without http://): ")
    try:
        conn = http.client.HTTPConnection(host)
        conn.request("GET", "/")
        res = conn.getresponse()
        print(Fore.GREEN + "\nHeaders:" + Style.RESET_ALL)
        print(res.headers)
    except Exception as e:
        print("Error:", e)

########################################################
elif num == 4:
    remote_host = input("Enter a host to scan: ")
    try:
        remote_ip = socket.gethostbyname(remote_host)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    print(f"Scanning {remote_ip}... (may take time)")
    try:
        for port in range(1, 10025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((remote_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
    except KeyboardInterrupt:
        print("Stopped by user.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Scan complete.")

########################################################
elif num == 5:
    url = input("Enter full URL (e.g., http://example.com): ")
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
        tag = input("Enter tag name to search (e.g., h1, title): ")
        found = soup.find(tag)
        print(Fore.GREEN + f"\nFirst <{tag}> found:" + Style.RESET_ALL, found)
    except Exception as e:
        print("Error:", e)

########################################################
elif num == 6:
    url = input("Enter full URL (e.g., http://example.com): ")
    try:
        page_text = BeautifulSoup(requests.get(url).text, 'html.parser').text
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page_text)
        if emails:
            print(Fore.GREEN + "Found emails:" + Style.RESET_ALL, emails)
        else:
            print("No emails found.")
    except Exception as e:
        print("Error:", e)

########################################################
elif num == 7:
    url = input("Enter full URL (e.g., http://example.com): ")
    try:
        page_text = BeautifulSoup(requests.get(url).text, 'html.parser').text
        # Simple phone number patterns (local and international)
        phones = re.findall(r"(?:\+\d{1,3}\s?)?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}", page_text)
        if phones:
            print(Fore.GREEN + "Found phone numbers:" + Style.RESET_ALL, phones)
        else:
            print("No phone numbers found.")
    except Exception as e:
        print("Error:", e)

else:
    print("Invalid option selected.")
