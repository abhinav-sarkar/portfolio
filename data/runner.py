import yahoo.data as data
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import TechnicalIndicator as ti

end = datetime.datetime.now()
begin = datetime.date(2012, 4, 29)
symbol = 'SPY'

df = data.get_symbol_prices_dataframe(symbol, begin, end)
print df
print df.dtypes
mov1 = ti.MovingAverage(df, window=12, type='exponential')
mov2 = ti.MovingAverage(df, window=26, type='exponential')
fr1 = ti.FRAMA(df, window=126, SC=300, FC=4)
fr2 = ti.FRAMA(df, window=98, SC=300, FC=4)
fr3 = ti.FRAMA(df, window=64, SC=300, FC=4)


data = pd.DataFrame()
data['Prices'] = df['Adj Close']
data['fast'] = fr3['frama']
data['med'] = fr2['frama']
data['slow'] = fr1['frama']


print data
plt.clf()
plt.plot(data.index, data)
plt.legend(data.columns)
plt.ylabel('Prices')
plt.xlabel('Date')
plt.show()
