class BaseModel:
    def __init__(self, returns):
        self.returns = returns

    def expected_returns(self):
        expected_returns = self.returns.mean()
        return expected_returns
    def expected_annual_returns(self):
        expected_annual_returns = self.returns.mean() * 252
        return expected_annual_returns