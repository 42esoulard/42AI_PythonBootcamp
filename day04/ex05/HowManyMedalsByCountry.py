#!/usr/bin/env python
# -*- coding: utf-8 -*-

def howManyMedalsByCountry(df, country):
	ctry = df[df['Team'] == country]
	ctry = ctry.drop_duplicates(["Team","NOC","Games","Year","Season","City","Sport","Event","Medal"])
	medals = {}
	for year in ctry['Year']:
		medals[year] = dict(ctry[ctry['Year'] == year]['Medal'].value_counts())
	lst = sorted(medals.keys())
	ordered = {}
	for year in lst: 
		ordered[year] = medals[year]
		try:
			gold = ordered[year]['Gold']
		except:
			gold = 0
		try:
			silver = ordered[year]['Silver']
		except:
			silver = 0
		try:
			bronze = ordered[year]['Bronze']
		except:
			bronze = 0
		ordered[year] = dict(G=gold, S=silver, B=bronze)
	print(ordered)