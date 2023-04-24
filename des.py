import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

import math

db = pd.read_csv("NFLX.csv")
db = db['Close'].to_numpy()


def double_exponential_smoothing(series, H=7, alpha=0.3, beta=0.3, return_all=False, y_test=False, fcast=False):
    """
    Given a series and alpha, return series of smoothed points
    Initialization: 
    S_1 = y_1, 
    b_1 = y_2 - y_1, 
    F_1 = 0, F_2 = y_1 
    level, S_t = alpha*y_t + (1-alpha)*(S_t-1 + b_t-1)
    trend, b_t = beta*(S_t - S_t-1) + (1-beta)*b_t-1
    forecast, F_t+1 = S_t + b_t
    forecast, F_t+m = S_t + m*b_t
    result[len(series)] is the estimate of series[len(series)]
    Inputs
        series: series to forecast
        H     : forecast horizon
        alpha : smoothing constant. 
                When alpha is close to 1, dampening is quick. 
                When alpha is close to 0, dampening is slow
        beta  : smoothing constant for trend
        return_all : if 1 return both original series + predictions, if 0 return predictions only
    Outputs
        the predictions of length H
    """
    result = [0, series[0]]   
    level = series[0]
    trend = series[1] - series[0]
    for n in range(1, len(series)+H-1):            
        if n >= len(series): # we are forecasting
            m = n - len(series) + 2
            result.append(level + m*trend) # result[len(series)+1] is the estimate of series[len(series)+1]
        else:
            value = series[n]
            last_level, level = level, alpha*value + (1-alpha)*(level+trend)
            trend = beta*(level-last_level) + (1-beta)*trend
            result.append(level+trend) 
            # e.g. result[2] uses series[1] 
            # ie. result[2] is the estimate of series[2]
            # e.g. result[len(series)] uses series[len(series)-1] 
            # ie. result[len(series)] is the estimate of series[len(series)]
    
    #if return_all == True:
    #    return result
    #else:
    #    return result[len(series):len(series)+H]
    return mean_squared_error(result[-H:], y_test), result
    



optimal_alpha = None
optimal_gamma = None
best_mse = math.inf

y_test = db[-7:]
fcast = None

for gamma in range(0,99):
    for alpha in range(0, 99):
        a, g = (alpha+1)*0.01, (gamma+1)*0.01
        mse, f = double_exponential_smoothing(db,7,a,g,False, y_test)
        if mse < best_mse:
            best_mse = mse
            optimal_alpha = a
            optimal_gamma = g
            fcast = f


print("Best MSE = %s" % best_mse)
print("Optimal alpha = %s" % optimal_alpha)
print("Optimal gamma = %s" % optimal_gamma)

plt.plot(db[-1000:],label = 'real data')
plt.plot(fcast[-1000:], label = 'forecast')
plt.legend()
plt.show()