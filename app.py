import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Prices through YFinance API
Shown are the **closing price** and **volume** of Google


""")

st.markdown('***Made with love by Raman***')

tickerSymbol=st.text_input("Ticker Symbol of the Stock", 'GOOGL')

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2010-6-23',end='2020-6-25')

st.write("Close")

st.line_chart(tickerDf.Close)

st.write("volume")

st.line_chart(tickerDf.Volume)

st.write("Open")

st.line_chart(tickerDf.Open)
