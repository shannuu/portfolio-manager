from src.portfolio.data.data_loader import DataLoader
from src.portfolio.data.data_cleaning import data_cleaning
from src.portfolio.data.returns import stocks_returns,market_returns

stocks_ticker = ["GOOGL", "JPM"]
market_ticker = "SPY"
total_ticker = stocks_ticker + [market_ticker]
start = "2025-11-10"
end = "2026-11-10"
loader = DataLoader(total_ticker, start, end)
prices = loader.load_prices()
closing_prices = data_cleaning(prices)

market_returns = market_returns(closing_prices, market_ticker)
stocks_returns = stocks_returns(closing_prices, stocks_ticker)

print(stocks_returns)
print(market_returns)