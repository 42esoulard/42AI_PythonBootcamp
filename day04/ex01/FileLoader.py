#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

class FileLoader():
	def load(self, path):
		rd = pd.read_csv(path)
		df = pd.DataFrame(rd)
		print("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1]))
		return df

	def display(self, df, n):
		if n > 0:
			print(df[:n])
		else:
			print(df[n:])