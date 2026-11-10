from src.portfolio.expected_returns.base_model import BaseModel
from src.portfolio.data.data_loader import DataLoader
from src.portfolio.data.data_cleaning import data_cleaning
from src.portfolio.data.returns import stocks_returns

stocks_ticker = ["GOOGL", "JPM"]
start = "2025-11-10"
end = "2026-11-10"
loader = DataLoader(stocks_ticker, start, end)
prices = loader.load_prices()
closing_prices = data_cleaning(prices)
returns = stocks_returns(closing_prices, stocks_ticker)

basemodel = BaseModel(returns)
expected_annual_returns = basemodel.expected_annual_returns()