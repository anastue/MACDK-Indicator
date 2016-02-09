import pandas as pd
from macdtester.basic import getTradingPeriods, isAnUpCrossingPoint


def getModifiedSignalLine(macd, signalLine, K):
    periods = getTradingPeriods(macd, signalLine)
    modifiedSignalLine = pd.Series(float('nan'), index=signalLine.index)

    for period in periods:
        avmin = getAvailablyMinimumPointsInAPeriod(macd, signalLine, period)
        avmax = getAvailablyMaximumPointsInAPeriod(macd, signalLine, period)    
        dmin = getMinimumCertainties(macd, signalLine, period)
        dmax = getMaximumCertainties(macd, signalLine, period)
        upCrossingPoint = None
        for t in period:
            if upCrossingPoint is None and isAnUpCrossingPoint(macd, signalLine, t):
                upCrossingPoint = t
                
            if upCrossingPoint is None:
                hMinimum = macd[avmin[t]] - signalLine[avmin[t]]
                modifiedSignalLine[t] = signalLine[t] + hMinimum*(dmin[t]**K)
            elif t == period[-1]:
                modifiedSignalLine[t] = signalLine[t]
            else:
                hMaximum = macd[avmax[t]] - signalLine[avmax[t]]
                modifiedSignalLine[t] = signalLine[t] + hMaximum*(dmax[t]**K)
      
    return modifiedSignalLine

def getModifiedSignalLineWithK(macd, signalLine):
    modifiedSignalLineWithK = pd.Series(float('nan'), index=signalLine.index)

    hmax=-9999999
    hmin=-9999999
    ht=1

    for t in signalLine.index:
    
        if (macd[t]>=signalLine[t]): 
            ht = macd[t] - signalLine[t]
        else:
            ht = signalLine[t] - macd[t]
                
        if (macd[t] >= signalLine[t]) and (macd[t] - signalLine[t])> hmax :
            hmax = macd[t] - signalLine[t]
        elif (signalLine[t]>=macd[t]) and (signalLine[t]-macd[t])> hmin:
            hmin = signalLine[t] - macd[t]
        if (hmax==-9999999 or hmin==-9999999):
             k=1
             m=1
        else:     
            k=(hmax+hmin)/(2*ht)
            m=(2*ht)/(hmax+hmin)
        
        if (signalLine[t] >= 0):
            if (macd[t] >= signalLine[t]):
                if (k<2):
                    modifiedSignalLineWithK[t]=signalLine[t]
                else:
                    modifiedSignalLineWithK[t]=signalLine[t]
                    
            elif (signalLine[t]>=macd[t]):
                if (m<0.5):
                    modifiedSignalLineWithK[t]=signalLine[t]*m
                else:
                        modifiedSignalLineWithK[t]=signalLine[t]
                    
        elif (signalLine[t] < 0):

            if (macd[t] >= signalLine[t]):
                if (m<0.7):
                    modifiedSignalLineWithK[t]=signalLine[t]
                else:
                     modifiedSignalLineWithK[t]=signalLine[t]
                    
            elif (signalLine[t]>=macd[t]):
                if (k<2):
                    modifiedSignalLineWithK[t]=signalLine[t]
                else:
                    modifiedSignalLineWithK[t]=signalLine[t]*k

    return modifiedSignalLineWithK

def getAvailablyMaximumPointsInAPeriod(macd, signalLine, period):
    avialablyMaximumPoints = pd.Series('', index=period)
    upCrossingPoint = None
    for t in period:
        if upCrossingPoint is None and isAnUpCrossingPoint(macd, signalLine, t):
            upCrossingPoint = t
        
        if upCrossingPoint is not None:
            avialablyMaximumPoints[t] = macd[upCrossingPoint:t].idxmax()
    
    return avialablyMaximumPoints

def getAvailablyMinimumPointsInAPeriod(macd, signalLine, period):
    avialablyMinimumPoints = pd.Series('', index=period)
    for t in period:
        if isAnUpCrossingPoint(macd, signalLine, t):
            avialablyMinimumPoints[t] = macd[period[0]:t].idxmin()
            break
        
        avialablyMinimumPoints[t] = macd[period[0]:t].idxmin()
    
    return avialablyMinimumPoints

def getMaximumCertainties(macd, signalLine, period):
    avmax = getAvailablyMaximumPointsInAPeriod(macd, signalLine, period)
    maximumCertainties = pd.Series('', index=period)
    upCrossingPoint = None
    for t in period:
        if t == period[-1]:
            maximumCertainties[t] = 1
            break
        
        if upCrossingPoint is None and isAnUpCrossingPoint(macd, signalLine, t):
            upCrossingPoint = t
        
        if upCrossingPoint is not None:
            hCurrent = macd[t] - signalLine[t]
            hMaximum = macd[avmax[t]] - signalLine[avmax[t]]
            maximumCertainties[t] = 1 - (hCurrent/float(hMaximum)) if hMaximum != 0 else 1
        
    return maximumCertainties

def getMinimumCertainties(macd, signalLine, period):
    avmin = getAvailablyMinimumPointsInAPeriod(macd, signalLine, period)
    minimumCertainties = pd.Series('', index=period)
    for t in period:
        if isAnUpCrossingPoint(macd, signalLine, t):
            minimumCertainties[t] = 1
            break
        
        hCurrent = macd[t] - signalLine[t]
        hMinimum = macd[avmin[t]] - signalLine[avmin[t]]
        minimumCertainties[t] = 1 - (hCurrent/float(hMinimum)) if hMinimum != 0 else 1
        
    return minimumCertainties
    
