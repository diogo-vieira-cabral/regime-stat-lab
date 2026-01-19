import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

print("=== 1H Intraday v4.0 (730d MAX) ===")

# YOUR EXACT original assets
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

end_date = datetime.now()
start_date = end_date - timedelta(days=730)

for name, ticker in assets.items():
    print(f"\n--- {name} 1H (730d) ---")
    data = yf.download(ticker, period="730d", interval='1h', progress=False)

    if data is not None and len(data) > 0:
        # Fix MultiIndex columns
        data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
        print("Columns:", data.columns.tolist())

        total_hours = len(pd.date_range(start=start_date, end=end_date, freq='h'))
        api_hours = len(data)

        print(f"Calendar: {total_hours}h, API: {api_hours}h ({api_hours/total_hours*100:.0f}%)")

        # Safe Close column handling
        if 'Close' in data.columns:
            data_clean = data.dropna(subset=['Close'])
        else:
            data_clean = data.dropna()

        data_clean.to_csv(f"{name}_1H_clean.csv")
        print(f"✅ Saved {len(data_clean)} hourly bars")
    else:
        print("❌ No data")

print("\n🎉 H1 pipeline complete - 12 CSVs generated!")
