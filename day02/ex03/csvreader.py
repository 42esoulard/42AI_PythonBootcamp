#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class CsvReader():
	def __init__(self, file, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = file
		pass

	def __enter__(self):
		try:
			self.fp = open(self.file, "r")
		except FileNotFoundError:
			print("File not found.")
			sys.exit()
		count = 0
		for line in self.fp:
			if count is self.skip_top:
				self.col = len(line.split(','))
			count += 1
		self.end = count - self.skip_bottom
		reader = 0
		self.fp.seek(0)
		for line in self.fp:
			if self.skip_top < reader < self.end:
				cp = line.split(',')
				ln = len(cp)
				for a in cp:
					if a.strip() is '':
						ln -= 1
				if ln is not self.col:
					return None
			reader += 1
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		self.fp.close()

	def getdata(self):
		res = ''
		reader = 0
		self.fp.seek(0)
		for line in self.fp:
			if (self.skip_top <= reader < self.end):
				res += line
			reader += 1
		return res

	def getheader(self):
		res = None
		if self.header is True:
			self.fp.seek(0)
			res = ''
			reader = 0
			for line in self.fp:
				if (reader < self.skip_top):
					res += line
				reader += 1
		return res


if __name__ == "__main__":
	with CsvReader('good.csv', header=True, skip_top=1) as file:
		data = file.getdata() 
		header = file.getheader()
		print(data)
		print(header)
	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")