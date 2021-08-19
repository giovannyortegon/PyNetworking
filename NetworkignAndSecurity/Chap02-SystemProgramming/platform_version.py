#!/usr/bin/env python3
from platform import python_implementation, python_version_tuple

print(python_implementation())

for attribute in python_version_tuple():
	print(attribute)
