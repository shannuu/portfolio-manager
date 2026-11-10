from src.portfolio.data.data_loader import DataLoader
from src.portfolio.data.data_cleaning import data_cleaning
from src.portfolio.data.returns import stocks_returns, market_returns

from src.portfolio.expected_returns.base_model import BaseModel
from src.portfolio.expected_returns.capm import CAPM

from src.portfolio.risk.covariance import calculate_covariance

from src.portfolio.optimization.mpt import mpt

import numpy as np

def capm_model(stocks_returns, market_returns, risk_free_rate):
    capm_model = CAPM(market_returns, stocks_returns, market_returns.mean()*252, risk_free_rate)
    expected_annual_returns = capm_model.expected_annual_returns()
    return expected_annual_returns

def base_model(stocks_returns):
    base_model = BaseModel(stocks_returns)
    expected_annual_returns = base_model.expected_annual_returns()
    return expected_annual_returns

def portfolio_pipeline(stock_tickers, market_ticker, start, end, model, risk_free_rate):
    total_tickers = stock_tickers + [market_ticker]
    
    # load data
    loader = DataLoader(total_tickers, start, end)
    prices = loader.load_prices()

    # Closing prices
    closing_prices = data_cleaning(prices)

    # returns
    stocks_returns_ = stocks_returns(closing_prices, stock_tickers)
    market_returns_ = market_returns(closing_prices, market_ticker)

    # expected returns
    if model == "capm":
        expected_annual_returns = capm_model(stocks_returns_, market_returns_, risk_free_rate)
    elif model == "base":
        expected_annual_returns = base_model(stocks_returns_)

    # covariance
    annual_covariance = calculate_covariance(stocks_returns_)

    # mpt
    mpt_model = mpt(stock_tickers, expected_annual_returns, annual_covariance, risk_free_rate)

    return mpt_model