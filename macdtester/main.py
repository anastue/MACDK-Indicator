from macdtester.data import getPricesData
from macdtester.tradingtest_originalmacd import originalMACDTest, getAllBuyPoints as org_getAllBuyPoints,\
    getAllSellPoints as org_getAllSellPoints, originalMACDTestWithSET100
from macdtester.macd import getMACDAndSignalLine
from macdtester.modifiedsignalline import getModifiedSignalLine
from macdtester.plot import standardPlot, addMarkers, addModifiedSignalLine
from macdtester.tradingtest_macdr1 import MACDR1Test, getAllBuyPoints as macdr1_getAllBuyPoints,\
    getAllSellPoints as macdr1_getAllSellPoints, MACDR1TestWithSET100
from macdtester.tradingtest_macdr2 import MACDR2Test, getAllBuyPoints as macdr2_getAllBuyPoints,\
    getAllSellPoints as macdr2_getAllSellPoints, MACDR2TestWithSET100
from macdtester.tradingtest_modifiedsignalline import modifiedSignalLineTest, getAllBuyPoints as modsig_getAllBuyPoints,\
    getAllSellPoints as modsig_getAllSellPoints,\
    modifiedSignalLineTestWithSET100
from macdtester.basic import getTradingPeriods, getMaximumPointsInAPeriod,\
    getMinimumPointsInAPeriod
from macdtester.tradingtest_modsigtradingweight import modsigTradingWeightTest, getAllBuyPoints as modsigw_getAllBuyPoints,\
    getAllSellPoints as modsigw_getAllSellPoints,\
    modsigTradingWeightTestWithSET100

## prepare data for a single data
print 'preparing data...'
symbol = 'KBANK'
pricesData = getPricesData(symbol)
macd, signalLine = getMACDAndSignalLine(pricesData, 12, 26, 9)
modifiedSignalLine = getModifiedSignalLine(macd, signalLine, 1)

pricesData = pricesData[25:]
macd = macd[25:]
signalLine = signalLine[25:]
modifiedSignalLine = modifiedSignalLine[25:]

## original MACD test with a single data
print 'original MACD test for ' + symbol
successRate, profitRate = originalMACDTest(pricesData, macd, signalLine)
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

allBuyPoints = org_getAllBuyPoints(pricesData, macd, signalLine)
allSellPoints = org_getAllSellPoints(pricesData, macd, signalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## MACDR1 test with a single data
print 'MACDR1 test for ' + symbol
successRate, profitRate = MACDR1Test(pricesData, macd, signalLine)
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

allBuyPoints = macdr1_getAllBuyPoints(pricesData, macd, signalLine)
allSellPoints = macdr1_getAllSellPoints(pricesData, macd, signalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## MACDR2 test with a single data
print 'MACDR2 test for ' + symbol
successRate, profitRate = MACDR2Test(pricesData, macd, signalLine)
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

allBuyPoints = macdr2_getAllBuyPoints(pricesData, macd, signalLine)
allSellPoints = macdr2_getAllSellPoints(pricesData, macd, signalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## modified signal line test with a single data
print 'modified signal line test for ' + symbol
successRate, profitRate = modifiedSignalLineTest(pricesData, macd, signalLine, modifiedSignalLine)
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

allBuyPoints = modsig_getAllBuyPoints(pricesData, macd, signalLine, modifiedSignalLine)
allSellPoints = modsig_getAllSellPoints(pricesData, macd, signalLine, modifiedSignalLine)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addModifiedSignalLine(fig, modifiedSignalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)

## modified signal line with trading weight test with a single data
print 'modified signal line with trading weight test for ' + symbol
successRate, profitRate = modsigTradingWeightTest(pricesData, macd, signalLine, modifiedSignalLine, 1)
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

allBuyPoints = modsigw_getAllBuyPoints(pricesData, macd, signalLine, modifiedSignalLine, 1)
allSellPoints = modsigw_getAllSellPoints(pricesData, macd, signalLine, modifiedSignalLine, 1)

fig = standardPlot(pricesData, macd, signalLine, show=False)
addModifiedSignalLine(fig, modifiedSignalLine, show=False)
addMarkers(fig, macd, allBuyPoints, color='#00CC00', show=False)
addMarkers(fig, macd, allSellPoints, color='#FF0000', show=True)



## original MACD test in SET-100
print 'original MACD test in SET-100'
successRate, profitRate = originalMACDTestWithSET100(verbose=True)
print 'original MACD test in SET-100'
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

## MACDR1 test in SET-100
print 'MACDR1 test in SET-100'
successRate, profitRate = MACDR1TestWithSET100(verbose=True)
print 'MACDR1 test in SET-100'
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

## MACDR2 test in SET-100
print 'MACDR2 test in SET-100'
successRate, profitRate = MACDR2TestWithSET100(verbose=True)
print 'MACDR2 test in SET-100'
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

## modified signal line test in SET-100
print 'modified signal line test in SET-100'
successRate, profitRate = modifiedSignalLineTestWithSET100(K=0.1, verbose=True)
print 'modified signal line test in SET-100'
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate
raw_input("Press Enter to continue...")

## modified signal line with trading weight test in SET-100
print 'modified signal line with trading weight test in SET-100'
successRate, profitRate = modsigTradingWeightTestWithSET100(K=0.1, R=1, verbose=True)
print 'modified signal line with trading weight test in SET-100'
print 'success rate: %f' % successRate
print 'profit rate: %f' % profitRate

