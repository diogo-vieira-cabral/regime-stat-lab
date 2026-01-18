import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

print("=== Missing Day Counter v3.0 (730d) ===")

assets = {
    'SP500': '^GSPC', 'NASDAQ': '^IXIC', 'DOWJONES': '^DJI',
    'BTC': 'BTC-USD', 'VIX': '^VIX', 
    'GOLD': 'GC=F', 'EURUSD': 'EURUSD=X', 'USDJPY': 'USDJPY=X'
}

end_date = datetime.now()
start_date = end_date - timedelta(days=730)
calendar = pd.date_range(start=start_date, end=end_date, freq='D')

for name, ticker in assets.items():
    print(f"\n--- {name} ---")
    data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), progress=False)

    if data is not None and len(data) > 0:
        # Fix MultiIndex columns
        data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]

        total_days = len(calendar)
        api_days = len(data)
        missing_days = total_days - api_days

        print(f"Calendar: {total_days}d, API: {api_days}d, Missing: {missing_days}d", end=" ")

        if missing_days > 0:
            print("⚠️")
            missing_dates = [d.strftime('%Y-%m-%d') for d in calendar if d not in data.index]
            print(f"Missing: {missing_dates[-3:]}")
        else:
            print("✅")

        data_clean = data.dropna(subset=['Close'])
        data_clean.to_csv(f"{name}_clean.csv")
        print(f"Saved {len(data_clean)} rows")
    else:
        print("❌ No data")
