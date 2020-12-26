#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def howManyMedals(df, name):
	athlete = df[df['Name'] == name]
	count = {}
	for year in athlete['Year']:
		count[year] = dict(athlete[athlete['Year'] == year]['Medal'].value_counts())
	for year in count:
		try:
			gold = count[year]['Gold']
		except:
			gold = 0
		try:
			silver = count[year]['Silver']
		except:
			silver = 0
		try:
			bronze = count[year]['Bronze']
		except:
			bronze = 0
		count[year] = dict(G=gold, S=silver, B=bronze)
	print(count)