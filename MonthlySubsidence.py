import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import pandas as pd

output = pd.DataFrame(columns=['Month', 'Sum', 'Count', 'Displacement'])

for filepath in glob.iglob('D:/mexico-monthly-sar-data/*.txt'):
    df = pd.read_csv(filepath, sep="\t")
    for col in df.columns:
        if 'coh' in col:
            df.rename(columns={col: "coh"}, inplace=True)

        if 'displacement' in col:
            df.rename(columns={col: "displacement"}, inplace=True)

    df = df[df.displacement != 0]
    df = df[df.coh > 0.3]

    
    output = output.append(pd.Series([filepath, df['displacement'].sum(), 
                                      df['displacement'].count(),(df['displacement'].sum()/df['displacement'].count())], 
                                     index=output.columns), ignore_index=True)

output.head()
output.to_csv("mexico-city-iztacalco-subsidence-2017")