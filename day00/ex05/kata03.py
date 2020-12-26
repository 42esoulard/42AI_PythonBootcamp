#!/usr/bin/env python
# -*- coding: utf-8 -*-

phrase = "The right format"

i = 42 - len(phrase)
k = 0
str = ''
for k in range(i):
	str += '-'
	k += 1
str += phrase
print(str, end = '')
