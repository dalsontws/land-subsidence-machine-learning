import numpy as np
import scipy.stats as st
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

df = pd.read_excel('mexico-municipal-population.xlsx')
df.head()

df.iloc[:, 1:] = df.iloc[:, 1:]/1000

numCols = df.shape[1]-1

# Create dataframe of training data (2013 and before)
df_train = df[df['Year'] <= 2013]

# Create dataframe of training data (2013 and before)
df_test = df[df['Year'] > 2013]


column = 'Álvaro Obregón'
X_train = df_train['Year'].values.reshape(-1,1)
y_train = df_train[column].values.reshape(-1,1)

X_test = df_test['Year'].values.reshape(-1,1)
y_test = df_test[column].values.reshape(-1,1)



# Train algorithm (normalization not required as there is only one feature)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print(y_pred)

# Creating a dataframe of test and predicted population values
df_check = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()}, index=X_test)

# Used for my own visualisation purpose: to show the difference in population data from 2014 to 2018
df_check.plot(kind='bar',figsize=(16,10))
plt.xticks(rotation='horizontal') 
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.show()

# Mean squared error of the estimator on the test data
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  

