import json
import openai

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf

openai.api_key = open('API_KEY', 'r').read()


def get_stock_price(ticker):
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)


def calculate_SMA(ticker, window):
    data = yr.Ticker(ticker).history(period='1y').Close
    return str(data.rolling(window=window).mean().iloc[-1])


def calculate_EMA(ticker, window):
    data = yr.Ticker(ticker).history(period='1y').Close
    return str(data.ewm(span=window, adjust=False).mean().iloc[-1])


def calculate_RSI(ticker, window):
    data = yr.Ticker(ticker).history(period='1y').Close
    delta = data.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=14-1, adjust=False).mean()
    ema_down = down.ewm(com=14-1, adjust=False).mean()
    rs = ema_up / ema_down
    return str(100-(100/(1+rs)).iloc[-1])


def calculate_MACD(ticker):
    data = yr.Ticker(ticker).history(period='1y').Close
    short_EMA = data.ewm(span=12, adjust=False).mean()
    long_EMA = data.ewm(span=26, adjust=False).mean()
