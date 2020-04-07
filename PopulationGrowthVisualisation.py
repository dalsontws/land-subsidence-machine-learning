import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('mexico-municipal-population.xlsx')

df.iloc[:, 1:] = df.iloc[:, 1:]/1000

numCols = df.shape[1]-1

# Initialize the figure
plt.style.use('seaborn-darkgrid')

num = 0
for column in df.drop('Year', axis=1):
    num += 1

    # Find the right spot on the plot
    plt.subplot(4, 5, num)

    # Plot the lineplot
    plt.plot(df['Year'], df[column], marker='', color='black',
             linewidth=1.9, alpha=0.9, label=column)

    plt.xlim(2000, 2020)
    plt.xticks(np.arange(2000, 2020, 1), rotation='vertical')

    # Add title
    plt.title(column, loc='left', fontsize=12,
              fontweight=0, color='black', y=1.08)
    plt.tight_layout()

# general title
plt.suptitle("Population Growth 2000-2020", fontsize=13,
             fontweight=0, color='black', style='italic', y=1.08)
