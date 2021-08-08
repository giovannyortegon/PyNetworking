#!/usr/bin/env python
import sys
try:
    import nmap
except:
    sys.exit("[!] Install the nmap library: pip install python-nmap")

# Argument Validator
if len(sys.argv) != 3:
    sys.exit("[!] Please provide two arguments the first being the targets the second the ports")

ports = str(sys.argv[2])
addrs = str(sys.argv[1])

scanner = nmap.PortScanner()
scanner.scan(addrs, ports)

for host in scanner.all_hosts():
    if not scanner[host].hostname():
        print("The host's IP address is %s and it's hostname was not found" %host)
    else:
        print("The host's IP address is %s and it's hostname is %s" %(host, scanner[host].hostname()))
