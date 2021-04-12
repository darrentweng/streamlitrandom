import yfinance as yf
import streamlit as st
import datetime

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

tickerSymbol = st.sidebar.text_input(
    "Stock ticker here",
    "GOOGL"
)
startdate = '2010-01-01'
enddate = '2010-01-01'
startdate = st.sidebar.date_input(label = 'Startdate input', value=(datetime.date(2019,7,6)))
enddate = st.sidebar.date_input(label = 'Enddate input', value=(datetime.date.today()))
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol   
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=startdate, end=enddate)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)