import yfinance as yf
import pandas as pd
import numpy as np

risk_free_rate = 4.87/100        # risk free rate (treasury bills)
stocks = ['GOOGL', 'MSFT', "JPM"]         # stocks
market_ticker = "SPY"        #benchmark (index)

req_data = stocks + [market_ticker]

data = yf.download(
    req_data,
    period = '1y',
    auto_adjust=True,
    progress=False
)

#--------------Downloading and cleaning data-----------------#
prices = data["Close"]
returns = prices.pct_change().dropna()
market_returns = returns["SPY"]
returns.drop("SPY", axis=1, inplace=True)
market_variance = market_returns.var()

#---Finding the covariance between stocks and benchmark------#
covariance = []
for i in range(len(stocks)):
    covariance.append(returns.iloc[:,i].cov(market_returns))

#--------------getting beta & expected returns---------------#
beta = np.array(covariance) / market_variance
expected_returns = beta*(market_returns.mean()*252 - risk_free_rate) + risk_free_rate

#-------------------printing the CAPM results----------------#
output_data = {
    "Beta": beta,
    "Historical Returns (%)": returns.mean()*252*100,
    "Expected Returns (%)": expected_returns*100
}
print("Annualized Historic Market Return: " + str(market_returns.mean()*252*100) + "%\n")
print(pd.DataFrame(output_data, index=stocks))