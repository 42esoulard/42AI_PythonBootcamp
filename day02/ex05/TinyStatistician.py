#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

class TinyStatistician():
	def mean(self, x):
		if x == []:
			return None
		i = 0
		res = 0
		for a in x:
			res += a
			i += 1
		res = res / i
		return (float(res))

	def median(self, x):
		if x == []:
			return None
		x.sort()
		i = 0
		for a in x:
			i += 1
		if i % 2 is 0:
			i = int(i/2)
			return (float((x[i - 1] + x[i]) / 2))
		return float(x[i//2])

	def quartile(self, x, percentile):
		if x == []:
			return None
		if percentile is 25:
			per = 1
		elif percentile is 75:
			per = 3
		x.sort()
		i = 0
		for a in x:
			i += 1
		if i % 4 * per is 0:
			i = int(i/4 * per)
			return (float((x[i - 1] + x[i]) / 2))
		return float(x[i//4 * per])

	def var(self, x):
		if x == []:
			return None
		mean = self.mean(x)
		res = list()
		for a in x:
			tmp = (a - mean)**2
			res.append(tmp)
		res1 = 0.0
		for a in res:
			res1 += a
		res1 = res1 / (len(res))
		return res1
	
	def std(self, x):
		if x == []:
			return None
		var = self.var(x)
		return sqrt(var)
