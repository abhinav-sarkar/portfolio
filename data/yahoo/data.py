import urllib2
import datetime
import pandas, StringIO
import numpy as np

def read_test_data(file):
    return pandas.read_csv(open(file, 'r'),
                           parse_dates=['Date'],
                           date_parser=lambda x: pandas.datetime.strptime(x, '%m/%d/%Y'),
                           index_col='Date')

def get_symbol_prices_dataframe(symbol, begin, end):
    return pandas.read_csv(StringIO.StringIO(get_symbol_price_csv(symbol, begin, end)),
                           parse_dates=['Date'],
                           date_parser=lambda x: pandas.datetime.strptime(x, '%Y-%m-%d'),
                           dtype={'Volume': np.float64},
                           index_col='Date')

def get_symbol_price_csv(symbol, begin, end):
    response = urllib2.urlopen(get_url(symbol, begin, end))
    val = response.read()
    lines = val.splitlines()
    newfile = list()
    newfile.append(lines[0]) #header

    for i in range(len(lines)-1, 0, -1):
        newfile.append(lines[i])

    return '\n'.join(newfile)


def get_url(symbol, begin, end):
    return "http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv" % (
        symbol, begin.month-1, begin.day, begin.year, end.month-1, end.day, end.year)