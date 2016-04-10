import urllib2
import datetime
import pandas, StringIO
import numpy as np

def get_price_csv(symbol, begin, end):
    url = get_url(symbol, begin, end)
    response = urllib2.urlopen(url)
    return response.read()

def get_url(symbol, begin, end):
    return "http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv" % (
        symbol, begin.month-1, begin.day, begin.year, end.month-1, end.day, end.year)

end = datetime.date(2016, 4, 4);
begin = datetime.date(2004, 4, 4);
symbol = 'AAPL'
prices = get_price_csv(symbol, begin, end)

output = StringIO.StringIO()
output.write(prices)
output.seek(0)
print pandas.read_csv(output, dtype={'Open': np.float64, 'Volume': np.float64})