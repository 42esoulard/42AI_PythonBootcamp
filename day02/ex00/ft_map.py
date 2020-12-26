#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ft_map(function_to_apply, list_of_inputs): 
	x = list()
	for a in list_of_inputs:
		x.append(function_to_apply(a))
	return x
	pass