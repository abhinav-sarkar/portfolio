import numpy as np
import pandas as pd
import math


def compute(a):
    print a
    return 1.0

def MovingAverage(data, window=30, columns=['Adj Close'], type='simple'):
    weights = None

    if type == 'simple':
        weights = np.ones(window)
    elif type == 'exponential':
        weights = np.linspace(-1.0, 0.0, window)
        weights = np.exp(weights)

    weights = weights / weights.sum()

    cols = [col for col in data if col not in columns]
    ma_data = data.drop(cols, axis=1, inplace=False)
    for col in columns:
        values = np.convolve(ma_data[col].values, weights, mode='full')
        values[:window] = np.nan
        ma_data[col] = values[:len(ma_data[col].values)]

    return ma_data

# Fractal Adaptive Moving Average
def FRAMA(data, window=6, SC=8, FC=2):
    if window%2 != 0:
        raise AssertionError('Window is not even')

    frama = data.copy()
    frama['Adj'] = frama['Adj Close']/frama['Close']
    frama['Adj High'] = frama['High'] * frama['Adj']
    frama['Adj Low'] = frama['Low'] * frama['Adj']

    frama['Hl1_h'] = frama['Adj High']
    frama['Hl1_l'] = frama['Adj Low']

    frama['Hl1_h'] = pd.rolling_apply(frama['Hl1_h'], window=window, func=lambda x: max(x[:window/2]), min_periods=window)
    frama['Hl1_l'] = pd.rolling_apply(frama['Hl1_l'], window=window, func=lambda x: min(x[:window/2]), min_periods=window)
    frama['Hl1'] = (frama['Hl1_h'] - frama['Hl1_l'])/window

    frama['Hl2_h'] = frama['Adj High']
    frama['Hl2_l'] = frama['Adj Low']

    frama['Hl2_h']=pd.rolling_apply(frama['Hl2_h'], window=window, func=lambda x: max(x[window / 2:]), min_periods=window)
    frama['Hl2_l']=pd.rolling_apply(frama['Hl2_l'], window=window, func=lambda x: min(x[window / 2:]), min_periods=window)
    frama['Hl2'] = (frama['Hl2_h'] - frama['Hl2_l']) / window

    frama['Hl_h'] = frama['Adj High']
    frama['Hl_l'] = frama['Adj Low']

    frama['Hl_h']=pd.rolling_apply(frama['Hl_h'], window=window, func=lambda x: max(x), min_periods=window)
    frama['Hl_l']=pd.rolling_apply(frama['Hl_l'], window=window, func=lambda x: min(x), min_periods=window)
    frama['Hl'] = (frama['Hl_h'] - frama['Hl_l']) / window

    frama['D'] = (np.log10(frama['Hl1']+frama['Hl2']) - np.log10(frama['Hl'])) / math.log(2.0, 10)
    W = math.log(2.0 / (SC + 1))
    frama['Alpha'] = np.exp(W*(frama['D']-1))
    frama['N'] = (2 - frama['Alpha']) / frama['Alpha']
    frama['NewN'] = ((SC - FC) * ((frama['N'] - 1) / (SC - 1))) + FC
    frama['NewAlpha'] = 2 / (frama['NewN'] + 1)
    frama['frama'] = frama['NewAlpha'] * np.NAN

    for i in range(window-1, len(frama.index)):
        ind = frama.index[i]
        indLast = frama.index[i-1]
        if np.isnan(frama['frama'].ix[indLast]):
            print frama['Adj Close'].ix[:ind]
            frama['frama'].ix[ind] = np.sum(frama['Adj Close'].ix[:ind])/(i+1)
            print frama
            #raw_input("First")
            continue

        #raw_input("Second")
        lastFrama = frama['frama'].ix[indLast]
        frama['frama'].ix[ind] = lastFrama + frama['NewAlpha'].ix[ind] * (frama['Adj Close'].ix[ind] - lastFrama)

    print frama
    print frama.dtypes
    return frama