import urllib2
import datetime
import pandas, StringIO
import numpy as np


def get_symbol_prices_dataframe(symbol, begin, end):
    return pandas.read_csv(StringIO.StringIO(get_symbol_price_csv(symbol, begin, end)),
                           parse_dates=['Date'],
                           date_parser=lambda x: pandas.datetime.strptime(x, '%Y-%m-%d'),
                           dtype={'Volume': np.float64},
                           index_col='Date')

def get_symbol_price_csv(symbol, begin, end):
    response = urllib2.urlopen(get_url(symbol, begin, end))
    return response.read()


def get_url(symbol, begin, end):
    return "http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv" % (
        symbol, begin.month-1, begin.day, begin.year, end.month-1, end.day, end.year)


end = datetime.date(2016, 4, 4);
begin = datetime.date(2004, 4, 4);
symbol = 'AAPL'

df = get_symbol_prices_dataframe(symbol, begin, end)
print df
print df.dtypes
