import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('data/mexico/mexico-city-weather.xlsx')
corr_matrix = df.corr(method='pearson')

f, ax = plt.subplots(figsize=(11, 15))

heatmap = sns.heatmap(corr_matrix,
                      square=True,
                      linewidths=.5,
                      cmap='coolwarm',
                      cbar_kws={'shrink': .4,
                                'ticks': [-1, -.5, 0, 0.5, 1]},
                      vmin=-1,
                      vmax=1,
                      annot=True,
                      annot_kws={"size": 12})

# add the column names as labels
ax.set_yticklabels(corr_matrix.columns, rotation=0)
ax.set_xticklabels(corr_matrix.columns)

b, t = plt.ylim()
b += 0.5
t -= 0.5
plt.ylim(b, t)

sns.set_style({'xtick.bottom': True}, {'ytick.left': True})

heatmap.get_figure().savefig('heatmap.png', bbox_inches='tight')
