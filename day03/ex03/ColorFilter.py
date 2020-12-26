#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class ColorFilter():
	def invert(self, array):
		ret = 1 - array
		return ret
	
	def to_blue(self, array):
		ret = array
		ret[0:,0:,:2] = 0
		return ret

	def to_green(self, array):
		ret = array
		ret[0:,0:,0::2] = 0
		return ret

	def to_red(self, array):
		ret = array
		ret[0:,0:,1:] = 0
		return ret

	def celluloid(self, array):
		a = np.linspace(0.0, 1, 5)
		ret = array
		ret[ret > a[2]] = a[2]
		ret[(a[1] < ret) & (ret < a[2])] = a[1]
		ret[(a[0] < ret) & (ret < a[1])] = a[0]
		return ret

	def to_grayscale(self, array, filter='w'):
		if filter.startswith('m'):
			sm = np.sum(array, 2)
			reshaped = np.reshape(sm, (array.shape[0], array.shape[1], 1))
			brd = np.broadcast_to(reshaped, (array.shape[0], array.shape[1], 3))
			ret = brd[:,:,:] / array.shape[2]
			return ret
		elif filter.startswith('w'):
			array[0:,0:,0] *= 0.299
			array[0:,0:,1] *= 0.587
			array[0:,0:,2] *= 0.114
			sm = np.sum(array, 2)
			ret = np.tile(sm[:,:,None], (1, 1, 3))
			return ret
			
import matplotlib.pyplot as plt


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
