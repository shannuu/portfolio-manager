def market_returns(prices,market_ticker):
    returns = prices[market_ticker].pct_change().dropna()
    return returns

def stocks_returns(prices, stocks_ticker):
    returns = prices[stocks_ticker].pct_change().dropna()
    return returns