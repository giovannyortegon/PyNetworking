#!/usr/bin/env python

fd = open("messages", "r")

for line in fd.readlines():
    ln = line.strip()
    if "USB" in ln:
        print ln
