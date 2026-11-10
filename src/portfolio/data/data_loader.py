import yfinance as yf

class DataLoader:
    def __init__(self, tickers, start, end):
        self.tickers = tickers
        self.start = start
        self.end = end

    def load_prices(self):
        data = yf.download(
            self.tickers,
            start = self.start,
            end = self.end,
            auto_adjust=True,
            progress=False
        )
        return data