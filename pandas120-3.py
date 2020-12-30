import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['simsun']})
data = pd.read_excel('600000.SH.xls')
print(data.head(3))

print(data.shape)
print(data.columns)
print(data[["开盘价(元)", "最高价(元)"]].mean(axis=0))
print(data[["开盘价(元)", "最高价(元)"]].dtypes)
print(data[data.isnull().any(axis=1)])
data.dropna(axis=0, how='any', inplace=True)
# print(data[data['日期'].isnull()])

data['收盘价(元)'].plot()
data[['收盘价(元)','开盘价(元)']].plot()
plt.show()