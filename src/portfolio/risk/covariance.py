import pandas as pd

def calculate_covariance(stocks_returns):
    annual_covariance = stocks_returns.cov() * 252
    return annual_covariance