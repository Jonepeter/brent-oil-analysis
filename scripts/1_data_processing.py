"""Minimal Brent oil data processing"""

import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path

def main():
    # Setup paths
    base_path = Path(__file__).parent.parent
    raw_dir = base_path / 'data' / 'raw'
    processed_dir = base_path / 'data' / 'processed'
    
    # Fetch Brent oil data
    brent = yf.download("BZ=F", start="1987-05-20", end="2024-12-31")
    df = pd.DataFrame({
        'Date': brent.index,
        'Price': brent['Close']
    }).dropna().reset_index(drop=True)
    
    # Add log returns
    df['log_returns'] = np.log(df['Price']).diff()
    
    # Save data
    df.to_csv(raw_dir / 'brent-oil-prices_raw.csv', index=False)
    df.to_csv(processed_dir / 'brent-oil-prices_cleaned.csv', index=False)
    
    print(f"✅ Processed {len(df)} observations ({df['Date'].min()} to {df['Date'].max()})")

if __name__ == "__main__":
    main()