#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class ScrapBooker():
	def crop(self, array, dimensions, position=(0,0)):
		size = array.shape
		if size[0] < dimensions[0] or size[1] < dimensions[1]:
			return ("ERROR")
		ret = array[position[0]:position[0]+dimensions[0], position[1]:position[1]+dimensions[1]]
		return (ret)

	def thin(self, array, n, axis):
		if axis is 0:
			ret = array[0:,0::n]
		elif axis is 1:
			ret = array[0::n,]
			
	def juxtapose(self, array, n, axis):
		res = array
		i = 1
		while i < n:
			res = np.concatenate((res, array), axis)
			i += 1
		return (res)

	def mosaic(self, array, dimensions):
		res = self.juxtapose(array, dimensions[0], 0)
		res = self.juxtapose(res, dimensions[1], 1)
		return (res)



import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor():
	def load(self, path):
		data = plt.imread(path)
		fig = plt.figure(path)
		arr = data.shape
		print("Loading image of dimensions {} x {}".format(arr[0], arr[1]))
		return data

	def display(self, array):
		plt.imshow(array)
		plt.show()
