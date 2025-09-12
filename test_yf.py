import yfinance as yf

# List of stocks you want to test
tickers = ["AAPL", "IDEA", "GOOGL"]

for ticker in tickers:
    print(f"\nDownloading data for {ticker}...")
    data = yf.download(ticker, start="2020-01-01", end="2025-09-12")
    if data.empty:
        print(f"❌ Failed to download data for {ticker}")
    else:
        print(f"✅ Data downloaded for {ticker}")
        print(data.head())
        print("Columns:", data.columns.tolist())
