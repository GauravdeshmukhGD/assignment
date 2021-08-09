#letsupgrade assignment

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#generate random data with numpy for 1000 data point with 2 columns
'''
df=pd.DataFrame (np.random.randn(1000,2))
print(df)
'''


#plot scatter plot ,line plot
'''

x=np.random.randn(40)
y=np.random.randn(40)
z=np.random.randn(40)
color=np.random.randn(40)
plt.title('scatter plot')
plt.scatter(x,y,s=z*10,c=color)
plt.show()

'''


#line plot
'''
x=np.arange (0,10)
y=np.arange (0,10)

plt.title('line plot')
plt.xlabel('xaxis')
plt.ylabel ('yaxis')
plt.plot(x,y,'r')
plt.show()
'''


#dataanalysis on bostan data

boston_dataset = load_boston()
print(boston_dataset.keys())
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston.head()
