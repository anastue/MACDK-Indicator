import pandas as pd
import pandas.stats.moments as mt

def getEMA(pricesData, n=12):
    ema = pd.Series(mt.ewma(pricesData, span=n), index=pricesData.index)
    return ema
