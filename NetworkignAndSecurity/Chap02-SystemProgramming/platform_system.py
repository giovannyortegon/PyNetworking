#!/usr/bin/env python3
import platform

operation_system = platform.system()

print("Your operation system is: ", operation_system)

if operation_system == "Windows":
	ping_command = "ping -n 100 -l 100 127.0.0.1"
elif operation_system == "Linux":
	ping_command = "ping -c 20 127.0.0.1"
else:
	ping_command = "ping -c 20 127.0.0.1"

print(ping_command)
