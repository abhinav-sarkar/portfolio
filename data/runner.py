import yahoo.data as data
import datetime
import TechnicalIndicator.MovingAverage as ma
import matplotlib.pyplot as plt
import pandas as pd

end = datetime.datetime.now()
begin = datetime.date(2013, 4, 29)
symbol = 'AAPL'

df = data.get_symbol_prices_dataframe(symbol, begin, end)
print df
print df.dtypes
mov1 = ma.simple_moving_average(df, 50, ['Adj Close'])
mov2 = ma.simple_moving_average(df, 100, ['Adj Close'])

data = pd.DataFrame()
data['Prices'] = df['Adj Close']
data['ma50'] = mov1['Adj Close']
data['ma100'] = mov2['Adj Close']

plt.clf()
plt.plot(data.index, data)
plt.legend(data.columns)
plt.ylabel('Prices')
plt.xlabel('Date')
plt.show()
