from src.portfolio.data.data_loader import DataLoader
from src.portfolio.data.data_cleaning import data_cleaning
from src.portfolio.data.returns import stocks_returns
from src.portfolio.risk.covariance import calculate_covariance
from src.portfolio.optimization.mpt import mpt
from src.portfolio.expected_returns.base_model import BaseModel

stocks_tickers = ["GOOGL", "JPM"]
start = "2025-11-10"
end = "2026-11-10"
risk_free_rate = 4.87/100

loader = DataLoader(stocks_tickers, start, end)

prices = loader.load_prices()
closing_prices = data_cleaning(prices)
stocks_returns = stocks_returns(closing_prices,stocks_tickers)

basemodel = BaseModel(stocks_returns)
expected_annual_returns = basemodel.expected_annual_returns()

annual_covariance_matrix = calculate_covariance(stocks_returns)
#print(annual_covariance_matrix)

tangency_portfolio, gmv_portfolio, gmv, max_sharpe = mpt(stocks_tickers, expected_annual_returns, annual_covariance_matrix, risk_free_rate)

print(tangency_portfolio, gmv_portfolio, gmv, max_sharpe)
print(expected_annual_returns)