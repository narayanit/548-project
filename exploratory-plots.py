import pandas as pd
import numpy as np

import plotly.express as px
import io

pd.options.plotting.backend = "plotly"

df = pd.read_csv("NFLX.csv")
print(df.head())

#plt.figure()
#plt.plot(df.Date, df.Close, )
#plt.show()  

#close plot

#close_sns = sns.lineplot(x=df.Date, y=df.Close, data = df)
#close_plot = close_sns.get_figure()
#close_plot.savefig("close.png")

fig = px.line(df, x='Date', y="Close")
fig.write_image("F-closeNFLX.png")

df['diffOC'] = df['Close'] - df['Open']
print(df.head())
print(df['diffOC'].head())

fig3 = px.line(df, x='Date', y='diffOC',title="Difference in Close and Open Stock Price 2002-2022").update_layout(xaxis_title="Date", yaxis_title="Close-Open")
fig3.write_image("F-Close-Open.png")

fig4 = px.line(df[df['Date']> '2021-06-03'], x='Date', y='diffOC',
title="Difference in Close and Open Stock Price 2021-2022").update_layout(xaxis_title="Date", yaxis_title="Close-Open")
fig4.write_image("F-Close-Open2019.png")

df['Range'] = df['High']-df['Close']

fig5 = px.line(df,x='Date', y='Range', title='Difference between the highest and lowest price on the given trading day')
fig5.write_image("F-Range.png")

fig6 = px.line(df[df['Date']>'2021-06-03'],x='Date', y='Range', title='Difference between the highest and lowest price on the given trading day')
fig6.write_image("F-Range2021.png")

fig7 = px.line(df, x='Date', y='Volume', title = 'Trading Volume')
fig7.write_image("F-TradingVolume.png")

### RELATIONSHIPS BETWEEN PAIRS OF VARIABLES ###

fig8 = px.line(df, x='Open', y='Close', title='Open vs Close price')
fig8.write_image("FR-OpenVSClose.png")

fig9 = px.line(df[df['Date']>'2019-06-03'], x='Open', y='Close', title='Open vs Close price')
fig9.write_image("FR-OpenVSClose2019.png")

fig10 = px.line(df, x='Close', y='Volume')
fig10.write_image("FR-ClosevsVolume.png")

fig11 = px.line(df[df['Date']>'2019-06-03'], x='Close', y='Volume')
fig11.write_image("FR-ClosevsVolume2019.png")
