#!/usr/bin/env python

from macdtester.macd import getMACDAndSignalLine
from macdtester.data import getPricesData
from macdtester.tradingtest_originalmacd import originalMACDTest, getAllBuyPoints as org_getAllBuyPoints,getAllSellPoints as org_getAllSellPoints, originalMACDTestWithSET100
from macdtester.modifiedsignalline import getModifiedSignalLine,getModifiedSignalLineWithK
from macdtester.plot import standardPlot, addMarkers, addModifiedSignalLine,addModifiedSignalLineWithK
from macdtester.tradingtest_macdr1 import MACDR1Test, getAllBuyPoints as macdr1_getAllBuyPoints, getAllSellPoints as macdr1_getAllSellPoints, MACDR1TestWithSET100
from macdtester.tradingtest_macdr2 import MACDR2Test, getAllBuyPoints as macdr2_getAllBuyPoints, getAllSellPoints as macdr2_getAllSellPoints, MACDR2TestWithSET100
from macdtester.tradingtest_modifiedsignalline import modifiedSignalLineTest, getAllBuyPoints as modsig_getAllBuyPoints, getAllSellPoints as modsig_getAllSellPoints, modifiedSignalLineTestWithSET100
from macdtester.tradingtest_modifiedsignalline_withK import modifiedSignalLineWithKtest, getAllBuyPoints as macdk_getAllBuyPoints, getAllSellPoints as macdk_getAllSellPoints, modifiedSignalLineWithKtestInSET100
from macdtester.tradingtest_modifiedsignalline_withK_1 import MACDK1Test, getAllBuyPoints as macdk1_getAllBuyPoints, getAllSellPoints as macdk1_getAllSellPoints, MACDK1TestWithSET100
from macdtester.tradingtest_modifiedsignalline_withK_2 import MACDK2Test, getAllBuyPoints as macdk2_getAllBuyPoints, getAllSellPoints as macdk2_getAllSellPoints, MACDK2TestWithSET100

## prepare data for a single data
print('preparing data...')
symbol=input("please input SET name: ")
if not symbol:raise Exception("Please Define SET")
symbol=symbol.upper()
pricesData = getPricesData(symbol)
macd, signalLine = getMACDAndSignalLine(pricesData, 12, 26, 9) #can change period later
modifiedSignalLine = getModifiedSignalLine(macd, signalLine, 1)
modifiedSignalLineWithK = getModifiedSignalLineWithK(macd, signalLine)

pricesData = pricesData[25:]
macd = macd[25:]
signalLine = signalLine[25:]
modifiedSignalLine = modifiedSignalLine[25:]
modifiedSignalLineWithK = modifiedSignalLineWithK[25:]

## modified signal line test with a single data
print('modified signal line with K test for ' + symbol)
successRate, profitRate = modifiedSignalLineWithKtest(pricesData, macd, modifiedSignalLineWithK)
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

allBuyPoints = macdk_getAllBuyPoints(pricesData, macd, modifiedSignalLineWithK)
allSellPoints = macdk_getAllSellPoints(pricesData, macd, modifiedSignalLineWithK)

fig = standardPlot(pricesData, macd, signalLine, show=True)
addModifiedSignalLineWithK(fig, modifiedSignalLineWithK, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## Modified signal Line with K-1 test with a single data
print('MACDK1 test for ' + symbol)
successRate, profitRate = MACDK1Test(pricesData, macd, modifiedSignalLineWithK)
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

allBuyPoints = macdk1_getAllBuyPoints(pricesData, macd, modifiedSignalLineWithK)
allSellPoints = macdk1_getAllSellPoints(pricesData, macd, modifiedSignalLineWithK)

fig = standardPlot(pricesData, macd, signalLine, show=True)
addModifiedSignalLineWithK(fig, modifiedSignalLineWithK, show=True)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=True)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## Modified signal Line with K-2 test with a single data
print('MACDK2 test for ' + symbol)
successRate, profitRate = MACDK2Test(pricesData, macd, modifiedSignalLineWithK)
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

allBuyPoints = macdk2_getAllBuyPoints(pricesData, macd, modifiedSignalLineWithK)
allSellPoints = macdk2_getAllSellPoints(pricesData, macd, modifiedSignalLineWithK)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addModifiedSignalLineWithK(fig, modifiedSignalLineWithK, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## original MACD test with a single data
print('Original MACD test for ' + symbol)
successRate, profitRate = originalMACDTest(pricesData, macd, signalLine)
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

allBuyPoints = org_getAllBuyPoints(pricesData, macd, signalLine)
allSellPoints = org_getAllSellPoints(pricesData, macd, signalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)


## MACDR1 test with a single data
print('MACDR1 test for ' + symbol)
successRate, profitRate = MACDR1Test(pricesData, macd, signalLine)
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

allBuyPoints = macdr1_getAllBuyPoints(pricesData, macd, signalLine)
allSellPoints = macdr1_getAllSellPoints(pricesData, macd, signalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## MACDR2 test with a single data
print('MACDR2 test for ' + symbol)
successRate, profitRate = MACDR2Test(pricesData, macd, signalLine)
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

allBuyPoints = macdr2_getAllBuyPoints(pricesData, macd, signalLine)
allSellPoints = macdr2_getAllSellPoints(pricesData, macd, signalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## Modified signal line test with a single data
print('Modified signal line test for ' + symbol)
successRate, profitRate = modifiedSignalLineTest(pricesData, macd, signalLine, modifiedSignalLine)
print('success rate: %f' % successRate)
print('profit rate: %f' % profitRate)
input("Press Enter to continue...")

allBuyPoints = modsig_getAllBuyPoints(pricesData, macd, signalLine, modifiedSignalLine)
allSellPoints = modsig_getAllSellPoints(pricesData, macd, signalLine, modifiedSignalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addModifiedSignalLine(fig, modifiedSignalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## Modified signal Line wit K test in SET 100
print('Modified signal Line wit K test in SET 100')
successRate, profitRate = modifiedSignalLineWithKtestInSET100(verbose=True)
print('Modified signal Line wit K test in SET 100')
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

## MACDK1 test in SET-100
print('MACDK1 test in SET-100')
successRate, profitRate = MACDK1TestWithSET100(verbose=True)
print('MACDK1 test in SET-100')
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

## MACDK2 test in SET-100
print('MACDK2 test in SET-100')
successRate, profitRate = MACDK2TestWithSET100(verbose=True)
print('MACDR2 test in SET-100')
print('success rate: %f' % successRate)
print('profit rate: %f' % profitRate)
input("Press Enter to continue...")

## Original MACD test in SET-100
print('Original MACD test in SET-100')
successRate, profitRate = originalMACDTestWithSET100(verbose=True)
print('Original MACD test in SET-100')
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

## MACDR1 test in SET-100
print('MACDR1 test in SET-100')
successRate, profitRate = MACDR1TestWithSET100(verbose=True)
print('MACDR1 test in SET-100')
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

## MACDR2 test in SET-100
print('MACDR2 test in SET-100')
successRate, profitRate = MACDR2TestWithSET100(verbose=True)
print('MACDR2 test in SET-100')
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")

## Modified signal line test in SET-100
print('Modified signal line test in SET-100')
successRate, profitRate = modifiedSignalLineTestWithSET100(K=0.1, verbose=True)
print('Modified signal line test in SET-100')
print('success rate: %s' % successRate)
print('profit rate: %s' % profitRate)
input("Press Enter to continue...")
