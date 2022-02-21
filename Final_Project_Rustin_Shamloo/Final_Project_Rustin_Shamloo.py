# Rustin Shamloo, DSCI 510 Final Project

# Dataset 1 - CoinCap API 2.0
# Source: https://docs.coincap.io/

import requests
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def scrape_coinbase():
    url = "https://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1451635200000&end=1613753794000"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers = headers, data = payload)
    json_data = json.loads(response.text.encode('utf8'))
    bitcoin_data = json_data["data"]
    df = pd.DataFrame(bitcoin_data)
    df = pd.DataFrame(bitcoin_data, columns = ['date', 'priceUsd'])
    df['priceUsd'] = pd.to_numeric(df['priceUsd'], errors = 'coerce').fillna(0, downcast = 'infer')
#     df.describe()
    for i in range(len(df)):
        df['date'].values[i] = df['date'].values[i].split('T')[0]
    print("This is the BTC dataset:")
    print(df)
    # df.to_csv('bitcoin-usd.csv', index = False)
    df.plot(x = 'date', y = 'priceUsd', kind = 'line', legend=None)
    plt.xticks(rotation=45)
    plt.title("BTC Price in USD")
    plt.show()
    change = ((53076.058942 - 433.122241) / 433.122241) * 100
    pct_x = (change / 100) * 1000
    print('----------------------------------------------------------------------------------')
    print('The price of BTC has increased ' + str(change) + " % in the past 5 years.")
    print("If you invested $1,000 in 2016 into BTC, you'd now have $" + str(pct_x) + " in today's dollars.")
    print('----------------------------------------------------------------------------------')

scrape_coinbase()

############################################################# 

# Dataset 2 - S&P 500 API
# Source: https://www.alphavantage.co/documentation/
# My free API Key is NR99A3HDFECIUH3T
import pandas as pd
import matplotlib.pyplot as plt
import requests

def scrape_stocks():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=SPY&apikey=NR99A3HDFECIUH3T'
    r = requests.get(url)
    data = r.json()
    data = data['Monthly Adjusted Time Series']
    df = pd.DataFrame(data)
    df = df.transpose()
    df = df.iloc[::-1]
    df['5. adjusted close'] = pd.to_numeric(df['5. adjusted close'], errors = 'coerce').fillna(0, downcast = 'infer')
    pd.to_datetime(df.index)
    # df.to_csv('sp500-final.csv', index = False)
    df2 = df[df.index > '2016-01-01']
    print("This is the S&P 500 ETF dataset:")
    print(df2)
    df2.plot(y = '5. adjusted close', kind = 'line', legend=None)
    plt.ylabel("Index Price (USD)")
    plt.title("S&P 500 ETF Price")
    plt.xticks(rotation=45)
    plt.show()
    change = ((459.2500 - 174.0895) / 174.0895) * 100
    pct_x = (change / 100) * 1000
    print('---------------------------------------------------------------------------------')
    print('The price of $SPY has increased ' + str(change) + " % in the past 5 years.")
    print("If you invested $1,000 in 2016 into the S&P 500 ETF, you'd now have $" + str(pct_x) + " in today's dollars.")
    print('---------------------------------------------------------------------------------')
    
scrape_stocks()

#############################################################    

# Dataset 3 - BLS.gov CPI 
# Source: https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def scrape_inflation():
    content = requests.get('https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems')
    soup = BeautifulSoup(content.content, 'html.parser')
    text = soup.get_text()
    text_spl = text.split('\n')
    lst = []
    for row in text_spl:
        row_spl = [value.strip() for value in row.split()]
        lst.append(row_spl)
    df = pd.DataFrame(lst[1:], columns = ['Series_ID', 'Year', 'Period', 'Value'])
    df = df.astype(str)
    df['Value'] = pd.to_numeric(df['Value'], errors = 'coerce').fillna(0, downcast = 'infer')
    df['Year'] = pd.to_numeric(df['Year'], errors = 'coerce').fillna(0, downcast = 'infer')
    print("This is the CPI dataset:")
    print(df)
    # df.to_csv('inflation.csv', index = False)
    df = df[df['Year'] >= 2016]
    df = df[df['Period'] == 'M01']
    df = df[df['Series_ID'] == 'CUSR0000SA0']
    # df.to_csv('inflation.csv', index = False)
    df.plot(x = 'Year', y = 'Value', kind = 'line', legend = None)
    plt.ylabel("Index Value")
    plt.xlabel("Year")
    plt.title("Consumer Price Index")
    plt.show()
    percent_change = ((262.231 - 237.652) / 237.652) * 100
    pv = (1 + (percent_change / 100)) * 1000
    print('------------------------------------------------------------------------------')
    print('We see a ' + str(percent_change) + ' % increase in inflation during the past 5 years.')
    print('To hedge against inflation, we would need to earn a ROI greater than this.')
    print('What cost you $1,000 to buy in 2016 now costs you $' + str(pv) + " today.")
    print('------------------------------------------------------------------------------')
       
scrape_inflation()

##############################################

import requests
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt

def scrape_coinbase_head():
    url = "https://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1451635200000&end=1613753794000"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers = headers, data = payload)
    json_data = json.loads(response.text.encode('utf8'))
    bitcoin_data = json_data["data"]
    df = pd.DataFrame(bitcoin_data)
    df = pd.DataFrame(bitcoin_data, columns = ['date', 'priceUsd'])
    df['priceUsd'] = pd.to_numeric(df['priceUsd'], errors = 'coerce').fillna(0, downcast = 'infer')
    for i in range(len(df)):
        df['date'].values[i] = df['date'].values[i].split('T')[0]
    print(df.head())

###############################################

import pandas as pd
import matplotlib.pyplot as plt
import time

def scrape_stocks_head():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=SPY&apikey=NR99A3HDFECIUH3T'
    r = requests.get(url)
    data = r.json()
    data = data['Monthly Adjusted Time Series']
    df = pd.DataFrame(data)
    df = df.transpose()
    df = df.iloc[::-1]
    df['5. adjusted close'] = pd.to_numeric(df['5. adjusted close'], errors = 'coerce').fillna(0, downcast = 'infer')
    pd.to_datetime(df.index)
    df2 = df[df.index >= '2016-01-01']
    print(df2.head())

#################################################
     
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def scrape_inflation_head():
    content = requests.get('https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems')
    soup = BeautifulSoup(content.content, 'html.parser')
    text = soup.get_text()
    text_spl = text.split('\n')
    lst = []
    for row in text_spl:
        row_spl = [value.strip() for value in row.split()]
        lst.append(row_spl)
    df = pd.DataFrame(lst[1:], columns = ['Series_ID', 'Year', 'Period', 'Value'])
    df = df.astype(str)
    df['Value'] = pd.to_numeric(df['Value'], errors = 'coerce').fillna(0, downcast = 'infer')
    df['Year'] = pd.to_numeric(df['Year'], errors = 'coerce').fillna(0, downcast = 'infer')
    print(df.head())
    df = df[df['Year'] >= 2016]
    df = df[df['Period'] == 'M01']
    df = df[df['Series_ID'] == 'CUSR0000SA0']
    
#################################################

import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import csv
import json

def default_function():
    print('This is the scraped Coinbase dataset:')
    scrape_coinbase()
    print('This is the scraped S&P500 ETF dataset:')
    scrape_stocks()
    print('This is the scraped Inflation dataset:')
    scrape_inflation()

def scrape_function():
    print('This is a sample of the scraped Coinbase dataset:')
    scrape_coinbase_head()
    print('This is a sample of the scraped S&P500 ETF dataset:')
    scrape_stocks_head()
    print('This is a sample of the scraped Inflation dataset:')
    scrape_inflation_head()

def static_function():
    print('This is a sample of the static Bitcoin dataset:')
    fhand = open('bitcoin-usd.csv', 'r')
    lines = fhand.readlines()
    for row in range(5):
        print(lines[row])

    print('This is a sample of the static S&P500 ETF dataset:')
    fhand = open('sp500-final.csv', 'r')
    lines = fhand.readlines()
    for row in range(5):
        print(lines[row])
            
    print('This is a sample of the static Inflation dataset:')
    fhand = open('inflation.csv', 'r')
    lines = fhand.readlines()
    for row in range(5):
        print(lines[row])
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        default_function()
        
    elif sys.argv[1] == '--scrape':
        scrape_function()

    elif sys.argv[1] == '--static':
        static_function()
#         path_to_static_data = sys.argv[2]
