import numpy as np

class CAPM:
    def __init__(self, market_returns, stock_returns, expected_market_returns, risk_free_rate):
        self.market_returns = market_returns
        self.stock_returns = stock_returns
        self.expected_market_returns = expected_market_returns
        self.risk_free_rate = risk_free_rate

    def expected_annual_returns(self):
        covariance = []
        for i in range(len(self.stock_returns.columns)):
            covariance.append(self.stock_returns.iloc[:,i].cov(self.market_returns))

        #--------------getting beta & expected returns---------------#
        beta = np.array(covariance) / self.market_variance
        expected_annual_returns = beta*(self.market_returns.mean()*252 - self.risk_free_rate) + self.risk_free_rate
        return expected_annual_returns