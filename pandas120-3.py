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

# df = data[~data[['换手率(%)']].applymap(np.isreal).any(axis=1)]
# df = df['换手率(%)'].apply(pd.to_numeric, errors='coerce')

# df = data[~data['换手率(%)'].apply(pd.api.types.is_number)]
df = data[data['换手率(%)'].apply(pd.api.types.is_number)]
df['换手率(%)'].plot(kind='kde')
# print(df.to_string())

# data['收盘价(元)'].plot()
# data[['收盘价(元)','开盘价(元)']].plot()
df = data['收盘价(元)'].diff()
df = data['收盘价(元)'].pct_change()
data = data.set_index('日期')
# df = data['收盘价(元)'].resample('W').max()

data['收盘价(元)'].plot()
data['收盘价(元)'].resample('7D').max().plot()
df = data['开盘价(元)'].expanding(min_periods=1).mean()
data['expanding Open mean']=data['开盘价(元)'].expanding(min_periods=1).mean()
data[['开盘价(元)', 'expanding Open mean']].plot(figsize=(16, 6))
data['former 30 days rolling Close mean']=data['收盘价(元)'].rolling(20).mean()
data['upper bound']=data['former 30 days rolling Close mean']+2*data['收盘价(元)'].rolling(20).std()#在这里我们取20天内的标准差
data['lower bound']=data['former 30 days rolling Close mean']-2*data['收盘价(元)'].rolling(20).std()
data[['收盘价(元)', 'former 30 days rolling Close mean','upper bound','lower bound' ]].plot(figsize=(16, 6))
# print(df.to_string())
# data['收盘价(元)'].plot()
# data['收盘价(元)'].rolling(5).mean().plot()
# data['收盘价(元)'].rolling(20).mean().plot()

plt.show()