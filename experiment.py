import pandas as pd
import numpy as np

x = np.random.uniform(1000,1001,size=(10000))
y = np.random.uniform(1000,1001,size=(10000))

d = {'x': x, 'y': y}
df = pd.DataFrame(d)
print(df.corr())