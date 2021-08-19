#!/usr/bin/env python3

try:
	myfile = open("newfile.txt", "wt")

	for i in range(10):
		myfile.write("Line #" + str(i + 1) + "\n")

	myfile.close()

except IOError as error:
	print("I/O error occurred: %s" %(str(error.errno)))
