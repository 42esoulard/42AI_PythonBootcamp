#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Evaluator():
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		total = 0
		#for a in words:
		#	total += len(a) * coefs[words.index(a)]
		for i, a in enumerate(words):
			total += len(a) * coefs[i]
		return total

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		total = 0
		#for a in words:
		#	total += len(a) * coefs[words.index(a)]
		for i, a in zip(coefs, words):
			total += len(a) * i
		return total