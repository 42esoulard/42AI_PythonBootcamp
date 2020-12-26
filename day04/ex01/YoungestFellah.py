#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def youngestFellah(df, year):
	
	ftab = df['Age'].where((df['Year'] == year) &
		(df['Sex'] == 'F'))
	mtab = df['Age'].where((df['Year'] == year) &
		(df['Sex'] == 'M'))
	f = np.amin(ftab)
	m = np.amin(mtab)
	print({'f': f, 'm': m})