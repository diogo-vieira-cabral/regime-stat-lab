import yfinance as yf
import pandas as pd

print("=== NaN Aware Fetcher v2.0 ===")

assets = {
    'SP500': '^GSPC', 'NASDAQ': '^IXIC', 'DOWJONES': '^DJI',
    'BTC': 'BTC-USD', 'VIX': '^VIX', 
    'GOLD': 'GC=F', 'EURUSD': 'EURUSD=X', 'USDJPY': 'USDJPY=X',
    'ES_fut': 'ES=F', 'NQ_fut': 'NQ=F', 'GOLD_fut': 'GC=F', 'CL_fut': 'CL=F'
}

for name, ticker in assets.items():
    print(f"\n--- {name} ---")
    data = yf.download(ticker, period="730d", progress=False)

    if data is not None and len(data) > 0:
        # Fix MultiIndex columns - flatten to simple names
        data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]

        total_rows = len(data)
        nan_rows = int(data.isna().any(axis=1).sum())
        nan_pct = (nan_rows / total_rows) * 100

        # Now safe to use 'Close'
        data_clean = data.dropna(subset=['Close'])
        clean_rows = len(data_clean)
        clean_pct = (clean_rows / total_rows) * 100

        print(f"Raw rows: {total_rows}")
        print(f"NaN rows: {nan_rows} ({nan_pct:.1f}%)")
        print(f"Clean rows: {clean_rows} ({clean_pct:.1f}%)")

        # Save raw + clean
        data.to_csv(f"{name}_raw.csv")
        data_clean.to_csv(f"{name}_clean.csv")
        print(f"✅ {name}_raw.csv + {name}_clean.csv")
    else:
        print(f"❌ {name}: No data")
