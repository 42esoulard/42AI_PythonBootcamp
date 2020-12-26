#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

def text_analyzer(str="", *rest):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if rest:
		print("ERROR")
		return
	if str is "":
		print("What is the text to analyze?")
		str = input()
	up = 0
	low = 0
	punc = 0
	sp = 0
	ot = 0
	for a in str:
		if a.isupper() == True:
			up += 1
		elif a.islower() == True:
			low += 1
		elif a.isspace() == True:
			sp += 1
		elif a in string.punctuation:
			punc += 1
		elif a.isnumeric():
			ot += 1
	print("The text contains", up + low + sp + punc + ot, "characters:")
	print("\n- ", up, "upper letters")
	print("\n- ", low, "lower letters")
	print("\n- ", punc, "punctuation marks")
	print("\n- ", sp, "spaces")