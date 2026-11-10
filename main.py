from src.portfolio.pipeline.portfolio_pipeline import portfolio_pipeline

def main():
    stocks = ["GOOGL", "JPM"]
    market = "SPY"
    start = "2025-11-10"
    end = "2026-11-10"
    risk_free_rate = 4.87/100
    model = "base"

    mpt_output = portfolio_pipeline(stocks, market, start, end, model, risk_free_rate)
    return mpt_output

if __name__ == "__main__":
    print(main())