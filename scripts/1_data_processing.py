"""
1_data_processing.py
Data collection and preprocessing for Brent oil analysis
"""

import yfinance as yf
import pandas as pd
import numpy as np
import os
from pathlib import Path

def fetch_brent_oil_data():
    """Fetch Brent oil data from Yahoo Finance"""
    ticker = "BZ=F"
    brent = yf.download(ticker, start="1987-05-20", end="2024-12-31")
    
    df = pd.DataFrame({
        'Date': brent.index,
        'Price': brent['Close']
    }).reset_index(drop=True)
    
    df = df.dropna()
    df['log_returns'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
    
    return df

def load_events_data():
    """Load geopolitical events data"""
    events_path = Path(__file__).parent.parent / 'data' / 'events_data.csv'
    return pd.read_csv(events_path)

def save_processed_data():
    """Process and save clean datasets"""
    # Create output directories
    raw_dir = Path(__file__).parent.parent / 'data' / 'raw'
    processed_dir = Path(__file__).parent.parent / 'data' / 'processed'
    
    raw_dir.mkdir(exist_ok=True)
    processed_dir.mkdir(exist_ok=True)
    
    # Fetch and save raw data
    df = fetch_brent_oil_data()
    events = load_events_data()
    
    # Save raw data
    df.to_csv(raw_dir / 'brent-oil-prices_raw.csv', index=False)
    
    # Process data
    df_clean = df.dropna()
    df_clean['Date'] = pd.to_datetime(df_clean['Date'])
    
    # Save processed data
    df_clean.to_csv(processed_dir / 'brent-oil-prices_cleaned.csv', index=False)
    
    print(f"✅ Data processing complete")
    print(f"📊 Raw data: {df.shape[0]} observations")
    print(f"🧹 Clean data: {df_clean.shape[0]} observations")
    print(f"📅 Date range: {df_clean['Date'].min()} to {df_clean['Date'].max()}")

if __name__ == "__main__":
    save_processed_data()