#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = ( 0, 4, 132.42222, 10000, 12345.67)

print("day_{:02}, ex_{:02} : {:.2f}, {:.2e}, {:.3}".format(
	t[0], t[1], t[2], float(t[3]), t[4]))