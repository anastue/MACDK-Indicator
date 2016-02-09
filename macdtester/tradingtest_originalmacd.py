import os
import pandas as pd
import numpy as np

from macdtester.basic import isAnUpCrossingPoint, isADownCrossingPoint, Trade, TotalTrade, getTradingPeriods
from macdtester.macd import getMACDAndSignalLine
from macdtester.data import getPricesData

def isABuyPoint(macd, signalLine, t):
    if isAnUpCrossingPoint(macd, signalLine, t):
        return True
    else:
        return False

def isASellPoint(macd, signalLine, t):
    if isADownCrossingPoint(macd, signalLine, t):
        return True
    else:
        return False

def getTotalTradesInAPeriod(macd, signalLine, period):
    tradeList = []
    buyPoint = None
    sellPoint = None
    capital = 1
    for t in period:
        if buyPoint is None and isABuyPoint(macd, signalLine, t):
            buyPoint = t
            
        if buyPoint is not None and isASellPoint(macd, signalLine, t):
            sellPoint = t
            
        if sellPoint is not None:
            tradeList.append(Trade(buyPoint, sellPoint, capital))
            buyPoint = None
            sellPoint = None
            
    if len(tradeList) > 0:
        return TotalTrade(tradeList)
    else:
        return None

def originalMACDTest(pricesData, macd, signalLine):
    periods = getTradingPeriods(macd, signalLine)
    profitRateList = []
    successList = []
    for period in periods:
        totalTrade = getTotalTradesInAPeriod(macd, signalLine, period)
        if totalTrade is not None:
            profitRate = totalTrade.getProfitRate(pricesData)
            profitRateList.append(profitRate)
            if profitRate > 0:
                successList.append(1)
            else:
                successList.append(0)
    
    if len(profitRateList) > 0:
        return np.mean(successList), np.mean(profitRateList)
    else:
        return None, None

def getAllBuyPoints(pricesData, macd, signalLine):
    periods = getTradingPeriods(macd, signalLine)
    allBuyPoints = []
    for period in periods:
        totalTrade = getTotalTradesInAPeriod(macd, signalLine, period)
        if totalTrade is not None:
            for trade in totalTrade.tradeList:
                allBuyPoints.append(trade.buyPoint)
    print('total buy' ,len(allBuyPoints))
    #print allBuyPoints
    return allBuyPoints

def getAllSellPoints(pricesData, macd, signalLine):
    periods = getTradingPeriods(macd, signalLine)
    allSellPoints = []
    for period in periods:
        totalTrade = getTotalTradesInAPeriod(macd, signalLine, period)
        if totalTrade is not None:
            for trade in totalTrade.tradeList:
                allSellPoints.append(trade.sellPoint)
    print('total sell' ,len(allSellPoints))
    #print allSellPoints
    return allSellPoints
    

def originalMACDTestWithSET100(verbose=False):
    directory = './resources/stockdata/'
    ignoreList = ['BANPU', 'MAKRO', 'VGI', 'STPI']
    symbolList = [f.replace('.csv','') for f in os.listdir(directory) if f.endswith('.csv') and f.split('.')[0] not in ignoreList]
    
    resultList = pd.DataFrame({'success rate': None, 'profit rate': None}, index=symbolList)
    
    for symbol in symbolList:
        if verbose: print('testing ' + symbol + '...')
        pricesData = getPricesData(symbol=symbol)
        macd, signalLine = getMACDAndSignalLine(pricesData, 12, 26, 9)
        
        pricesData = pricesData[25:]
        macd = macd[25:]
        signalLine = signalLine[25:]
        successRate, profitRate = originalMACDTest(pricesData, macd, signalLine)

        getAllBuyPoints(pricesData, macd, signalLine)
        getAllSellPoints(pricesData, macd, signalLine)

        
        resultList['profit rate'][symbol] = profitRate
        resultList['success rate'][symbol] = successRate
        
    if verbose:
        import webbrowser
        f = open(os.getcwd() + '/temp.html', 'w')
        f.write('Original MACD test with SET-100')
        f.write(resultList.to_html())
        f.close()
        webbrowser.open(os.getcwd() + '/temp.html', new=2)

    
    resultList = resultList.dropna()
    avgSuccessRate = resultList['success rate'].mean()
    avgProfitRate = resultList['profit rate'].mean()
    return avgSuccessRate, avgProfitRate
        
        
        
        
        
        
        
        
