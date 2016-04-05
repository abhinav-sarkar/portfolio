import urllib2
import datetime


def get_price(symbol, begin, end):
    url = "http://real-chart.finance.yahoo.com/table.csv?s=AAPL&a=11&b=12&c=1980&d=00&e=4&f=2016&g=d&ignore=.csv"
    response = urllib2.urlopen(url)
    html = response.read()
    print html

def get_url(symbol, begin, end):
    return "http://real-chart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=1980&d=00&e=4&f=2016&g=d&ignore=.csv" % (
        symbol, begin.month-1, begin,)
