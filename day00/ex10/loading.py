#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ft_progress(lst):
	for i in lst:
		print("ETA:")

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)