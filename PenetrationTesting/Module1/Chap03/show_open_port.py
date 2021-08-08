#!/usr/bin/env python3

from scapy.all import *

ip = "127.0.0.1"

dst_port = 80

headers=IP(dst=ip)/TCP(dport=dst_port, flags="S")

answers,unanswers=sr(headers,timeout=10)
