#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

class NumPyCreator():
	def from_list(self, lst):
		return numpy.array(lst)

	def from_tuple(self, tpl):
		return numpy.asarray(tpl)

	def from_iterable(self, itr):
		return numpy.asarray(list(itr))

	def from_shape(self, shape, value=0):
		ret = numpy.zeros(shape)
		ret.shape = shape
		return ret

	def random(self, shape):
		ret = numpy.random.rand(numpy.prod(shape))
		ret.shape = shape
		return ret

	def identity(n):
		return numpy.identity(n)