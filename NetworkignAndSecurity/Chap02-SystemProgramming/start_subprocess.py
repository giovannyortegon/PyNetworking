#!/usr/bin/env python3
import subprocess

process = subprocess.Popen(["python3", "--version"])
print(process)
process.terminate()
