#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

class Vector(object):
	def __init__(self, arg):
		self.values = list()
		i = 0
		if isinstance(arg, list):
				try:
					self.values = arg
					[float(i) for i in self.values] 
					self.size = len(arg)
					print(self.values, self.size)
				except:
					sys.exit(1)
		elif isinstance(arg, int):
			try:
				self.size = int(arg)
				self.values = [*range(0, self.size)]
				[float(i) for i in self.values] 
				print(self.values, self.size)
			except:
				sys.exit(1)
		elif isinstance(range(*arg), range):
			try:
				self.values = [*range(*arg)]
				[float(i) for i in self.values] 
				self.size = len(range(*arg))
				print(self.values, self.size)
			except:
				sys.exit(1)
	
	def __add__(self, other):
		if type(other) is type(self):
			if self.size != other.size:
				sys.exit(1)
			res = Vector(self.size)
			i = 0
			while i < res.size:
				res.values[i] = self.values[i] + other.values[i]
				print("CALCUL ", self.value[i], '+', other.value[i], "=", self.values[i] + other.values[i])
				#print(res.values[i], self.values[i], other.values[i])
				i += 1
		elif isinstance(self, Vector) and (isinstance(other, int) or isinstance(other, float)):
			res = Vector(self.size)
			i = 0
			while i < res.size:
				res.values[i] = self.values[i] + other
				print("CALCUL ", self.values[i], '+', other, "=", self.values[i] + other)
				print(res.values[i], self.values[i], other)
				i += 1
		print("RESULT", res)
		return res

	def __radd__(self, other):
		return self + other
	# add : scalars and vectors, can have errors with vectors. 

	def __sub__(self, other):
		if type(other) is type(self):
			if self.size != other.size:
				sys.exit(1)
			res = Vector(self.size)
			i = 0
			while i < res.size:
				res.values[i] = self.values[i] - other.values[i]
				print(res.values[i], self.values[i], other.values[i])
				i += 1
		elif isinstance(self, Vector) and (isinstance(other, int) or isinstance(other, float)):
			res = Vector(self.size)
			i = 0
			while i < res.size:
				res.values[i] = self.values[i] - other
				print(res.values[i], self.values[i], other)
				i += 1
		print("RESULT", res)
		return res

	def __rsub__(self, other):
		return self - other
	# sub : scalars and vectors, can have errors with vectors. 

	def __truediv__(self, other):
		if (type(other) is int or type(other) is float) and (type(self) is int or type(self) is float) :	
			print("RESULT", res)
			return self / float

	def __rtruediv__(self, other):
		if (type(other) is int or type(other) is float) and (type(self) is int or type(self) is float) :	
			print("RESULT", res)
			return self / float
	# div : only scalars.

	def __mul__(self, other):
		if type(other) is type(self):
			if self.size != other.size:
				sys.exit(1)
			res = Vector(self.size)
			i = 0
			while i < res.size:
				res.values[i] = self.values[i] * other.values[i]
				print(res.values[i], self.values[i], other.values[i])
				i += 1
			i = 0
			dot = 0
			while i < res.size:
				dot += res.values[i]
				print(dot)
				i += 1
		elif isinstance(self, Vector) and (isinstance(other, int) or isinstance(other, float)):
			res = Vector(self.size)
			i = 0
			while i < res.size:
				res.values[i] = self.values[i] * other
				print(res.values[i], self.values[i], other)
				i += 1
		print("RESULT", res)
		return res

	def __rmul__(self, other):
		return self * other
	# mul : scalars and vectors, can have errors with vectors,
	# return a scalar if we perform Vector * Vector (dot product)

	def __str__(self):
		res = "(Vector {})".format(self.values)
		return res

	def __repr__(self):
		res = "Vector {}".format(self.values)
		return res





