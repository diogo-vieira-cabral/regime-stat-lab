import yfinance as yf
import pandas as pd

print("=== Daily Data Fetcher v1.0 ===")

assets = {
    'SP500': '^GSPC',
    'NASDAQ': '^IXIC',
    'DOWJONES': '^DJI',
    'BTC': 'BTC-USD',
    'VIX': '^VIX',
    'GOLD': 'GC=F',
    'EURUSD': 'EURUSD=X',
    'USDJPY': 'USDJPY=X',
    'ES': 'ES=F',
    'NQ': 'NQ=F',
    'GOLD_futures': 'GC=F',  
    'CL_futures': 'CL=F'
}

for name, ticker in assets.items():
    data = yf.download(ticker, start="2025-01-01", progress=False)
    if data is not None and len(data) > 0:
        data.to_csv(f"{name}.csv")
        print(f"✅ {name}: {len(data)} days")
    else:
        print(f"❌ {name}: No data")