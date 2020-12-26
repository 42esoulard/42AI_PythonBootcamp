#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def error():
	print("ERROR")
	return

if len(sys.argv) == 2:
	num = sys.argv[1]
	try:
		num = int(num)
		if num is 0:
			print("I'm Zero.")
		elif num % 2 is 0:
			print("I'm Even.")
		else:
			print("I'm Odd.") 
	except:
		error()
else:
	error()