#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

i = 2
str = sys.argv[1]
while i < len(sys.argv):
	str = ''.join([str, ' '])
	str = ''.join([str, sys.argv[i]])
	i += 1
newstr = ''
for a in str:
	if (a.isupper()) == True:
		newstr += a.lower()
	elif (a.islower()) == True:
		newstr += a.upper()
	else:
		newstr += a
str = newstr[::-1]
print(str)