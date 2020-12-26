#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def usage():
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("	python operations.py 10 3")

if len(sys.argv) > 3:
	print("InputError: too many arguments\n")
	usage()
elif len(sys.argv) < 3:
	usage()
else:
	try:
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[2])
		print("Sum:		", num1 + num2)
		print("Difference:	", num1 - num2)
		print("Product:	", num1 * num2)
		if num2 is 0:
			print("Quotient:	 ERROR (div by zero)")
			print("Remainder:	 ERROR (modulo by zero)")
		else:
			print("Quotient:	", num1 / num2)
			print("Remainder:	", num1 % num2)
	except:
		print("InputError: only numbers\n")
		usage()