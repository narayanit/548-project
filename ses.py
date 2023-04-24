import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from sklearn.metrics import mean_squared_error


df = pd.read_csv("NFLX.csv", parse_dates=["Date"], index_col="Date")

df.index = pd.DatetimeIndex(df.index).to_period('D')

rows = df.shape[0]

train = df.iloc[:4035]
test = df.iloc[4035:5043]
#check there is no intersection


ses = SimpleExpSmoothing(train['Close'])
alpha = 0.2
model = ses.fit(smoothing_level=alpha, optimized=True)

fit1 = SimpleExpSmoothing(train['Close'], initialization_method="heuristic").fit(
    smoothing_level=0.2, optimized=False
)
fcast1 = fit1.forecast(7).rename(r"$\alpha=0.2$")

fit2 = SimpleExpSmoothing(train['Close'], initialization_method="heuristic").fit(
    smoothing_level=0.6, optimized=False
)
fcast2 = fit2.forecast(7).rename(r"$\alpha=0.6$")

fit3 = SimpleExpSmoothing(train['Close'], initialization_method="estimated").fit()
fcast3 = fit3.forecast(7).rename(r"$\alpha=%s$" % fit3.model.params["smoothing_level"])


plt.figure(figsize=(12, 8))
close = train['Close'].iloc[900:].to_numpy()
plt.plot(close, color="black")
plt.plot(fit1.fittedvalues.iloc[900:].to_numpy(), color="blue")
(line1,) = plt.plot(fcast1.iloc[900:].to_numpy(), color="blue")
plt.plot(fit2.fittedvalues.iloc[900:].to_numpy(), color="red")
(line2,) = plt.plot(fcast2.iloc[900:].to_numpy(), color="red")
plt.plot(fit3.fittedvalues.iloc[900:].to_numpy(), color="green")
(line3,) = plt.plot(fcast3.iloc[900:].to_numpy(), color="green")
plt.legend([line1, line2, line3], [fcast1.name, fcast2.name, fcast3.name])
plt.savefig("SES.png")


Y_true = test.iloc[0:7]['Close']
mse1 = mean_squared_error(fcast1, Y_true)
mse2 = mean_squared_error(fcast2, Y_true)
mse3 = mean_squared_error(fcast3, Y_true)
print(mse1, mse2, mse3)

# seven days 244.27356595715577 48.6037202363932 16.376126191597944
# hundred days 905.4247762083759 677.2950618747003 633.0744403971067

