import yfinance as yf
import streamlit as st
import datetime
import numpy as np
import pandas as pd

Snp500=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Stonks!
""")

stocks = st.sidebar.multiselect(
    "Stock tickers here",
    Snp500['Symbol'].tolist()
)
startdate = '2010-01-01'
enddate = '2010-01-01'
startdate = st.sidebar.date_input(label = 'Startdate input', value=(datetime.date(2019,7,6)))
enddate = st.sidebar.date_input(label = 'Enddate input', value=(datetime.date.today()))
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol   
#get data on this ticker
haveResult = False
firstable = True

for s in stocks:
    #get the historical prices for this ticker
    tickerDf = yf.Ticker(s).history(period='1d', start=startdate, end=enddate)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    if firstable == True:
        voldf = tickerDf[['Volume']].rename(columns={'Volume':s})
        outputdf = tickerDf[['Close']].rename(columns={'Close':s})
        firstable = False
    else:
        outputdf[s] = tickerDf['Close']
        voldf[s] = tickerDf['Volume']
    haveResult = True

if haveResult:
    st.line_chart(outputdf)
    st.line_chart(voldf) 