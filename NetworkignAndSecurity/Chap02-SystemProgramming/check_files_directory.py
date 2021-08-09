#!/usr/bin/env python3
import os

for root, directories, files in os.walk(".", topdown=False):
	# Iterate over the files in current root
	for file_entry in files:
		# create the ralative path to the files
		print("[+] ", os.path.join(root, file_entry))

	for name in directories:
		print("[++] ", name)
