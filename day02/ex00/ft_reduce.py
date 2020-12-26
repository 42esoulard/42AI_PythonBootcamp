#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ft_reduce(function_to_apply, list_of_inputs): 
	x = list_of_inputs[0]
	i = 1
	while i < len(list_of_inputs):
		x = function_to_apply(x, list_of_inputs[i])
		i += 1
	return x

	pass