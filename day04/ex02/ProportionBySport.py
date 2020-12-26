#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def proportionBySport(df, year, sport, gender):
	total = df[(df['Year'] == year) & (df['Sex'] == gender)]['ID'].nunique()
	spec = df[(df['Year'] == year) & (df['Sex'] == gender) 
		& (df['Sport'] == sport)]['ID'].nunique()
	percent = spec / total
	print(percent)
