#!/usr/bin/env python3

try:
	countlines = countchars = 0

	f = open("newfile.txt", 'r')
	lines = f.readlines()

	for line in lines:
		countlines += 1

		for char in line:
			countchars += 1

	f.close()

	print("Characters in files: %s" %countchars)
	print("Lines in file: %s" %countlines)

except IOError as error:
	print("I/O error occurred: %s" %(str(error)))
