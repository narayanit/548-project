import pandas as pd
import numpy as np

df = pd.read_csv("NFLX.csv")

#print(df.describe())
#print(df[df['Date']>'2019-06-03'].describe())
#print(df[df['Date']>'2021-06-03'].describe())

print(df.nlargest(1,columns = ['Close']))
### close peaked at 2021-11-17  690.0  700.98999  686.090027  691.690002  691.690002  2732800

print(df.nlargest(3,columns = ['Volume']))
### highest trading volume on  2004-10-15  1.432857  1.641429  1.422857  1.471429   1.471429  
### Date       Open       High        Low      Close  Adj Close     Volume
### 2004-10-15   1.432857   1.641429   1.422857   1.471429   1.471429  323414000
### 2011-10-25  10.700000  11.341429  10.607143  11.052857  11.052857  315541800
### 2011-09-20  20.200001  20.425714  18.481428  18.575714  18.575714  224343000
# Trading volume is the total number of shares of a security that were traded during a given period of time. 
# A reversal is when the direction of a price trend has changed, from going up to going down, or vice-versa.

print(df[df['Close']!=df['Adj Close']].shape[0])
#Adjusted Close was never different, so no corporate actions adjusted the close price

cols = ['Open', 'Close', 'High', 'Low', 'Adj Close', 'Volume']

correlation = df[cols].corr()
print(correlation)