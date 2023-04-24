import pandas as pd
import numpy as np

from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split

import statsmodels.api as sm

import plotly.express as px
import io

pd.options.plotting.backend = "plotly"

df = pd.read_csv("NFLX.csv")

cols = ['Open', 'Close', 'High', 'Low', 'Adj Close', 'Volume']

correlation = df[cols].corr()
print(correlation)

x = df[['Open', 'Close', 'High', 'Low', 'Adj Close', 'Volume']]
x = x.to_numpy()

y = df['Close']
y = y.to_numpy()

#separating the dataset in train and test set
#20% used for testing - the last four years
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)


#choosing a model - just a basic linear regression
model1 = sm.OLS(y_train, X_train).fit()
#print(model1.summary())

with open('summary1.txt', 'w') as fh:
    fh.write(model1.summary().as_text())

predictions = model1.predict(X_test)
df_results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})

fig = px.line(df_results, x='Actual', y='Predicted')
fig.write_image("M-Predicitons.png")

