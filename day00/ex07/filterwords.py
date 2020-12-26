#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string

if len(sys.argv) is 3 and sys.argv[1].isnumeric() is False:
	try:
		inp = sys.argv[1].split()
		min = int(sys.argv[2])
		res = list()
		for a in inp:
			for b in a:
				if b in string.punctuation:
					a = a.replace(b, '')
			if int(len(a)) > min:
				res.append(a)
		print(res)
	except:
		print("ERROR")
else:
	print("ERROR")