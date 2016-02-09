#!/usr/bin/env python3
import numpy as np

def getTradingPeriods(macd, signalLine):
    downCrossingPoints = getDownCrossingPoints(macd, signalLine)
    periods = []
    for i in range(len(downCrossingPoints)-1):
        periods.append(macd[downCrossingPoints[i]:downCrossingPoints[i+1]].index)
    return periods
        

def isAnUpCrossingPoint(macd, signalLine, t):
    i = macd.index.get_loc(t)
    
    if i >= 1 and (macd.ix[i] > signalLine.ix[i]) and (macd.ix[i-1] < signalLine.ix[i-1]):
        return True
    elif i >= 2 and (macd.ix[i] > signalLine.ix[i]) and (macd.ix[i-1] == signalLine.ix[i-1]) and (macd.ix[i-2] < signalLine.ix[i-2]):
        return True
    else:
        False

def isADownCrossingPoint(macd, signalLine, t):
    i = macd.index.get_loc(t)
    
    if i >= 1 and (macd.ix[i] < signalLine.ix[i]) and (macd.ix[i-1] > signalLine.ix[i-1]):
        return True
    elif i >= 2 and (macd.ix[i] < signalLine.ix[i]) and (macd.ix[i-1] == signalLine.ix[i-1]) and (macd.ix[i-2] > signalLine.ix[i-2]):
        return True
    else:
        False

def getUpCrossingPoints(macd, signalLine):
    upCrossingPointList = []
    firstDownCrossingExists = False
    for t in macd.index:
        if not firstDownCrossingExists and isADownCrossingPoint(macd, signalLine, t):
            firstDownCrossingExists = True
            
        if firstDownCrossingExists and isAnUpCrossingPoint(macd, signalLine, t):
            upCrossingPointList.append(t)
            
    return upCrossingPointList

def getDownCrossingPoints(macd, signalLine):
    downCrossingPointList = []
    for t in macd.index:
        if isADownCrossingPoint(macd, signalLine, t):
            downCrossingPointList.append(t)
            
    return downCrossingPointList

class Trade(object):
    def __init__(self, buyPoint, sellPoint, capital, weight=1):
        self.buyPoint = buyPoint
        self.sellPoint = sellPoint
        self.capital = capital
        self.weight = weight
        
    def getProfit(self, pricesData):
        return ((pricesData[self.sellPoint] - pricesData[self.buyPoint])/float(pricesData[self.buyPoint]))*self.capital*self.weight

class TotalTrade(object):
    def __init__(self, tradeList):
        self.initialCapital = tradeList[0].capital
        for trade in tradeList:
            if trade.capital != self.initialCapital:
                raise Exception('All trade in tradeList must have the same capital.')
            
        self.tradeList = tradeList
        
    def getProfitRate(self, pricesData):
        if len(self.tradeList) == 1:
            profitRate = self.tradeList[0].getProfit(pricesData)/float(self.initialCapital)
        else:
            profits = np.array([trade.getProfit(pricesData) for trade in self.tradeList])
            profitRate = np.sum(profits)/float(self.initialCapital - np.sum(profits[profits < 0]))
            
        return profitRate

def getUpCrossingPointInAPeriod(macd, signalLine, period):
    upCrossingPoint = None
    for t in period:
        if isAnUpCrossingPoint(macd, signalLine, t):
            upCrossingPoint = t
            break
        
    return upCrossingPoint

def getMaximumPointsInAPeriod(macd, signalLine, period):
    upCrossingPoint = None
    for t in period:
        if isAnUpCrossingPoint(macd, signalLine, t):
            upCrossingPoint = t
            break

    maximumPoint = macd[upCrossingPoint:period[-1]].idxmax()
    
    return maximumPoint

def getMinimumPointsInAPeriod(macd, signalLine, period):
    upCrossingPoint = None
    for t in period:
        if isAnUpCrossingPoint(macd, signalLine, t):
            upCrossingPoint = t
            break

    minimumPoint = macd[period[0]:upCrossingPoint].idxmin()
    
    return minimumPoint
        
        
