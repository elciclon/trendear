import yfinance as yf
import pandas as pd
import streamlit as st


# Read csv file
tickers_list = pd.read_csv("stocks.csv").values.flatten().tolist()

# Download data
data: pd.DataFrame = yf.download(tickers=tickers_list, start="2023-04-01")

# Filter by close prices
close_prices = data.loc[:, "Close"].copy()

# Normalize the close prices
normalized_close = close_prices.div(close_prices.iloc[0].mul(100))

st.line_chart(normalized_close)
