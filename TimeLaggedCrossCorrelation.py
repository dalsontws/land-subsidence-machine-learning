import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def df_derived_by_shift(df,lag=0,NON_DER=[]):
    df = df.copy()
    if not lag:
        return df
    cols ={}
    for i in range(1,lag+1):
        for x in list(df.columns):
            if x not in NON_DER:
                if not x in cols:
                    cols[x] = ['{}_{}'.format(x, i)]
                else:
                    cols[x].append('{}_{}'.format(x, i))
    for k,v in cols.items():
        columns = v
        dfn = pd.DataFrame(data=None, columns=columns, index=df.index)    
        i = 1
        for c in columns:
            dfn[c] = df[k].shift(periods=i)
            i+=1
        df = pd.concat([df, dfn], axis=1, join_axes=[df.index])
    return df


df = pd.read_excel('data/mexico/monthly/mexico-city-all-final.xlsx')

fields = ['Month', 'Rainfall','Displacement'] 
x = df[fields]

rainfall = df['Rainfall'].values
displacement = df['Displacement'].values

NON_DER = ['Month', 'Displacement']
df_new = df_derived_by_shift(x, 6, NON_DER)
df_new.head()

df_new = df_new.dropna()
df_new.corr()

colormap = plt.cm.RdBu
plt.figure(figsize=(15,10))
plt.title(u'6 months', y=1.05, size=16)

mask = np.zeros_like(df_new.corr())
mask[np.triu_indices_from(mask)] = True

svm = sns.heatmap(df_new.corr(), mask=mask, linewidths=0.1,vmax=1.0, 
            square=True, cmap=colormap, linecolor='white', annot=True)

svm.get_figure().savefig('TimeLaggedCrossCorrelation.png', bbox_inches='tight')