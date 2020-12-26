#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SpatioTemporalData(object):
	_metadata = ['added_property']
	added_property = 1

	@property
	def _constructor(self):
			return SubclassedDataFrame

	def __init__(self, data): 
			self.df = data

	def when(self, location):
		dates = self.df[self.df["City"] == location]['Year'].unique()
		print(list(dates))

	def where(self, date):
		loc = self.df[self.df["Year"] == date]['City'].unique()
		print(list(loc))