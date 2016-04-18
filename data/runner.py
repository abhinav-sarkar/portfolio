import yahoo.data as data
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import TechnicalIndicator as ti

end = datetime.datetime.now()
begin = datetime.date(2013, 4, 29)
symbol = 'AAPL'

df = data.get_symbol_prices_dataframe(symbol, begin, end)
print df
print df.dtypes
mov1 = ti.MovingAverage(df, window=12, type='exponential')
mov2 = ti.MovingAverage(df, window=26, type='exponential')
fr = ti.FRAMA(df)

data = pd.DataFrame()
data['Prices'] = df['Adj Close']
data['ma50'] = mov1['Adj Close']
data['ma100'] = mov2['Adj Close']
data['frama'] = fr['frama']


print data
plt.clf()
plt.plot(data.index, data)
plt.legend(data.columns)
plt.ylabel('Prices')
plt.xlabel('Date')
plt.show()
