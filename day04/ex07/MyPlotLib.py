#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import seaborn as sns

class MyPlotLib():
	def histogram(self, data, features):
		fig, ax = plt.subplots(1, len(features))
		uniq = data.drop_duplicates(['Name'])
		i = 0
		for feature in features:
			if uniq.dtypes[feature] != np.object:
				df = uniq[feature]
				ax[i].set_title(feature)
				ax[i].hist(df)
				ax[i].grid()
				i += 1
		plt.show()

	def density(self, data, features):
		uniq = data.drop_duplicates(['Name'])
		uniq[features].plot.kde()
		plt.show()

	def pair_plot(self, data, features):
		uniq = data.drop_duplicates(['Name'])
		sns.pairplot(uniq[features], kind='scatter', plot_kws={'edgecolor':None, 's': 10, 'alpha': 0.3})
		plt.show()

	def box_plot(self, data, features):
		uniq = data.drop_duplicates(['Name'])
		flierprops = {'marker':'o', 'markersize':8, 'color':'black', 'markerfacecolor':'None'}
		medianprops = {'color':'yellowgreen'}
		boxprops = {'linestyle':'-', 'color':'deepskyblue'}
		whiskerprops = {'color':'deepskyblue', 'linewidth':1}
		ax = sns.boxplot(data=uniq[features], flierprops=flierprops, medianprops=medianprops,
			boxprops=boxprops, whiskerprops=whiskerprops, width=0.2)

		plt.setp(ax.artists, alpha=.5, linewidth=1, fill=False, edgecolor="deepskyblue")
		plt.show()

rd = pd.read_csv("../resources/athlete_events.csv")
df = pd.DataFrame(rd)
#hist = df.hist(column='Height')
mpl = MyPlotLib()
mpl.box_plot(df, ['Weight', 'Height'])


