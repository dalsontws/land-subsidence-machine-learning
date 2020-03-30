import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

subsidence = pd.read_excel(
    'data/mexico/mexico-yearly-subsidence.xlsx').dropna()
population = pd.read_excel('data/mexico/population-density-2015.xlsx')
subsidence = subsidence.sort_values(by=['Municipal'])
population = population.sort_values(by=['Municipality'])

ax1 = sns.barplot(y="Municipal", x="2016 mean", data=subsidence, color="blue")

ax2 = sns.barplot(y="Municipality", x="Pop Density (2015)",
                  data=population, color="blue")
