#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ft_filter(function_to_apply, list_of_inputs): 
	x = list()
	if function_to_apply is None:
		for a in list_of_inputs:
			if a is True:
				x.append(a)
	else:
		for a in list_of_inputs:
			if function_to_apply(a) is True:
				x.append(a)
	return x
	pass