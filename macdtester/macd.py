import pandas as pd
import pandas.stats.moments as mt

from macdtester.ema import getEMA

def getMACDAndSignalLine(pricesData, n1, n2, n3):
    ema_n1 = getEMA(pricesData, n1)
    ema_n2 = getEMA(pricesData, n2)
    macd = ema_n1 - ema_n2
    signalLine = pd.Series(mt.ewma(macd, span=n3), index=pricesData.index)
    return macd, signalLine
