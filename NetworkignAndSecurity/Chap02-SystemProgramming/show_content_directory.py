#!/usr/bin/env python3
import os

pwd = os.getcwd()
:x

list_directory = os.listdir(pwd)

for directory in list_directory:
	print(directory)
