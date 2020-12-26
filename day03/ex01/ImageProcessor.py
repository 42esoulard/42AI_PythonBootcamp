#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
