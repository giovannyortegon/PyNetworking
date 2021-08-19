#!/usr/bin/env python3
import subprocess
import sys
import argparse


parser = argparse.ArgumentParser(description="Ping Scan Nertwork")
parser.add_argument("-network", dest="network",
					help="Network segment [for example 192.168.1]",
					required=True)
parser.add_argument("-machines", dest="machines", help="Machines number",
					type=int, required=True)

parsed_args = parser.parse_args()

for ip in range(40, parsed_args.machines+1):
	ipAddress = parsed_args.network + '.' + str(ip)
	print("Scanning %s " %(ipAddress))

	if sys.platform.startswith('linux'):	# Linux
		output = subprocess.Popen(["/bin/ping", "-c 1",
		ipAddress], stdout = subprocess.PIPE).communicate()[0]
	elif sys.platform.startswith("win"):	# Windows
		output = subprocess.Popen(["ping", ipAddress],
		stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0]
		output = output.decode("utf-8")

#	print("Output ", output)
	if b"Lost = 0" in output or b"bytes from " in output:
		print("The Ip Address %s has responded with a ECHO_REPLY!" % ipAddress)
