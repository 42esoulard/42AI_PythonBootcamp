#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

def generator(text, sep=" ", option=None):
	if isinstance(text, str) is False or option is not None and option is not 'shuffle' and option is not 'unique' and option is not 'ordered':
		print("ERROR")
		sys.exit()
	spl = text.split(sep)
	if option == "unique":
		new = list(dict.fromkeys(spl))
	elif option == "ordered":
		new = sorted(spl, key=lambda t: (t[0][0].isupper(), t[0]))
	elif option == "shuffle":
		new = spl
		for i in range(len(spl)):
			n = str(time.time())[-1]
			j = int(n)
			if j < len(new):
				new[i], new[j] = new[j], new[i]
	new = iter(new)
	for word in new:
		yield word

