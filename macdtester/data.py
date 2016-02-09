import pandas as pd

class DataDefinition (str):
    def __new__(cls, name, colNumber, dtype):
        return str.__new__(cls, name)
    
    def __init__(self, name, colNumber, dtype):
        super(DataDefinition, self).__init__(name)
        self.colNumber = colNumber
        self.dtype = dtype
        

DATE = DataDefinition('date', 0, 'S8')
OPEN = DataDefinition('open', 1, 'f8')
HIGH = DataDefinition('high', 2, 'f8')
LOW = DataDefinition('low', 3, 'f8')
CLOSE = DataDefinition('close', 4, 'f8')

def _getRawData(uri='./resources/stockdata/KBANK.csv'):
    data = pd.read_csv(uri, dtype={DATE: DATE.dtype,
                               OPEN: OPEN.dtype, HIGH: HIGH.dtype,
                               LOW: LOW.dtype, CLOSE: CLOSE.dtype,
                               }, parse_dates=[0], index_col=0, na_values='-')
    
    return data.sort_index(ascending=True).dropna()

def getPricesData(symbol='KBANK', type='close'):
    if type not in [OPEN, HIGH, LOW, CLOSE]:
        raise Exception('param-value error: type= "' + type +'". Hint, type=x for x in {"open", "high", "low", "close"}')
    uri = './resources/stockdata/' + symbol + '.csv'
    
    rawData = None
    try:
        rawData = _getRawData(uri)
    except:
        raise Exception('error occur while parsing raw data. Hint, please check if symbol="' + symbol + '" exists and matches the name of csv file.')
    
    data = rawData[type]
    return data
