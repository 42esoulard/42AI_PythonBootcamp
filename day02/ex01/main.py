#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def what_are_the_vars(*args, **kwargs): 
	i = 0
	obj = ObjectC()
	for a in args:
		setattr(obj, "var_{}".format(i), a)
		i += 1
	for key, value in kwargs.items():
		for a in dir(obj):
			if key is a:
				return None
		setattr(obj, key, value)
	return obj
	pass

class ObjectC(object): 
	def __init__(self):
		pass

def doom_printer(obj): 
	if obj is None:
		print("ERROR") 
		print("end") 
		return
	for attr in dir(obj): 
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value)) 
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world") 
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)