import pandas as pd

# Simple Moving Average
def simple_moving_average(data, period=30, sma_columns=['Adj Close']):
    cols = [col for col in data if col not in sma_columns]
    sma = pd.rolling_mean(
        data.drop(cols,
            axis=1,
            inplace=False),
        window=period,
        min_periods=period)
    return sma