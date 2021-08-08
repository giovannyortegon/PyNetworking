#!/usr/bin/env python3

import sys
try:
    from scapy.all import *
#    from scapy import *
except:
    sys.exit("[!] Install scapy libraries with: pip install scapy")

ip = "127.0.0.1"
icmp = IP(dst=ip) / ICMP()
#resp = sr1(icmp, timeout=10)
answers, unanswers = sr1(icmp, timeout=10)

#if resp == None:
#    print("The host is down")
#else:
#    print("The host is up")
sent, received = answers[80]
