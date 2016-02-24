import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, font_manager

class IndexManager(object):

    def __init__(self, indexSeries):
        self.index = indexSeries
        self.evenlyIndex = pd.Series(np.arange(len(indexSeries)), index=indexSeries)

    def evenlyIndexToDateTimeIndex(self, x):
        try:
            return self.index[x]
        except:
            return None

    def datetimeIndexToEvenlyIndex(self, d):
        try:
            return self.evenlyIndex[d]
        except:
            return None

    def dateMappingFormatter(self, x, pos=None):
        dmf = self.evenlyIndexToDateTimeIndex(int(x + 0.5))
        if dmf is not None:
            d1,dmf,d2=dmf.split("\'")
            #TODO
            y = dmf[0:4]
            m = dmf[4:6]
            d = dmf[6:8]
            #return dmf.strftime('%b\n%Y')
            return '%s\n%s'%(m,y)
        else:
            return '' 

def standardPlot(pricesData, macd, signalLine, show=True):
    idm = IndexManager(pricesData.index)
    plt.rc('axes', grid=False)
    #set grid
    plt.rc('grid', color='0.75', linestyle='-', linewidth=0.1)
    
    left, width = 0.1, 0.8
    rect1 = [left, 0.6, width, 0.3]
    rect2 = [left, 0.1, width, 0.5]
    
    
    fig = plt.figure(facecolor='white')
    axescolor  = '#f9f9f9'  # the axes background color
    ax1 = fig.add_axes(rect1, axisbg=axescolor)  #left, bottom, width, height
    ax2 = fig.add_axes(rect2, axisbg=axescolor, sharex=ax1)
    
    
    #we don't want to label all indices, just the first day in each month are enough
    #this function return the list of the (evenly) indices of the first day in each month
    def getIndexOfFirstDayEachMonth(datearr):
        #dateSeries = pd.Series(datearr.month)
        dateSeries = pd.Series(datearr)
        isFirstDay = np.ones_like(dateSeries, dtype=np.bool)
        isFirstDay[1:] = (dateSeries[1:] != dateSeries[:-1])
        return dateSeries.index[isFirstDay]
        
    #we then use the above mentioned list as a 'FixedLocator' and set it as the major locator 
    ax1.xaxis.set_major_locator(ticker.FixedLocator(getIndexOfFirstDayEachMonth(pricesData.index)))
    
    #only the indices in the locator will be labeled, the plotter will ask the 'formatter' which labels corresponds to which indices
    #this is the place where our mapping is used
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(idm.dateMappingFormatter))
    
    #set nice left and right spaces
    ax1.set_xlim(idm.evenlyIndex[0] - 2, idm.evenlyIndex[-1] + 2)
    
    ax1.plot(idm.evenlyIndex, pricesData, color='black', lw=2, label='closing price')
    ax2.plot(idm.evenlyIndex, macd, color='red', lw=1.5, label='MACD Line')
    ax2.plot(idm.evenlyIndex, signalLine, color='blue', lw=1, label='Signal Line')
    
    for label in ax1.get_xticklabels():
        label.set_visible(False)

    ax1.yaxis.set_major_locator(ticker.MaxNLocator(5, prune='both'))
    ax2.yaxis.set_major_locator(ticker.MaxNLocator(5, prune='both'))
    
    props = font_manager.FontProperties(size=10)
    leg1 = ax1.legend(loc='best', shadow=True, fancybox=True, prop=props, scatterpoints=1, markerscale=1)
    leg1.get_frame().set_alpha(0.5) 
    leg2 = ax2.legend(loc='best', shadow=True, fancybox=True, prop=props, scatterpoints=1, markerscale=1)
    leg2.get_frame().set_alpha(0.1)
    #if show: plt.show()
    return fig

def addModifiedSignalLine(fig, modifiedSignalLine, color='violet', show=True):
    idm = IndexManager(modifiedSignalLine.index)
    ax2 = fig.get_axes()[1]
    ax2.plot(idm.evenlyIndex, modifiedSignalLine, color=color, lw=1, label='Modified Signal Line')
    path = "resources/files/macd.png"
    if show:plt.savefig(path)
    #if show: plt.show()
    return fig

def addMarkers(fig, macd, tList, markerSize=20, color='#00CC00', show=True):
    idm = IndexManager(macd.index)
    ax2 = fig.get_axes()[1]
    ax2.scatter(idm.evenlyIndex[tList], macd[tList], color=color, s=markerSize)
    path = "resources/files/macd.png"
    if show:plt.savefig(path)
    #if show: plt.show()
    return fig

def addModifiedSignalLineWithK(fig, modifiedSignalLineWithK, color='orange', show=True):
    idm = IndexManager(modifiedSignalLineWithK.index)
    ax2 = fig.get_axes()[1]
    ax2.plot(idm.evenlyIndex, modifiedSignalLineWithK, color='orange', lw=1, label='Modified Signal Line With K')
    props = font_manager.FontProperties(size=10)
    leg2 = ax2.legend(loc='best', shadow=True, fancybox=True, prop=props, scatterpoints=1, markerscale=1)
    leg2.get_frame().set_alpha(0.5)
    path = "resources/files/macd.png"
    if show:plt.savefig(path)
    #if show: plt.show()
    return fig
    
    
