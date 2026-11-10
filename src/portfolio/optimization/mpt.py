import numpy as np
import pandas as pd

def mpt(stocks, expected_annual_returns, annual_covariance, risk_free_rate):
    epochs = 10000
    port_returns=[]
    port_risk=[]

    tangency_portfolio = []
    max_sharpe = 0
    gmv = 1
    gmv_portfolio = []
    
    for i in range(epochs):
        weights = np.random.dirichlet(np.ones(len(stocks))) # dirichlet method to have a balanced weight distributition
        port_return = np.dot(weights,expected_annual_returns)
        port_returns.append(port_return) # find the returns and risk of the portfolio for each portfolio
        port_var = weights.T @ annual_covariance @ weights # risk of the portfolio
        port_risk.append(port_var**0.5)
        sharpe = (port_return - risk_free_rate)/(port_var**0.5)
        if sharpe > max_sharpe:
            max_sharpe = sharpe
            tangency_portfolio = weights
        if port_var < gmv:
            gmv = port_var
            gmv_portfolio = weights

    return tangency_portfolio, gmv_portfolio, gmv, max_sharpe