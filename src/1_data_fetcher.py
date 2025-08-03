import yfinance as yf
import pandas as pd
import os

def fetch_brent_oil_data():
    """Fetch real Brent oil data from Yahoo Finance"""
    # Brent oil ticker symbol
    ticker = "BZ=F"  # Brent crude oil futures
    
    # Fetch data from 1987 to present
    brent = yf.download(ticker, start="1987-05-20", end="2024-12-31")
    
    # Reset index to get Date as column
    brent = brent.reset_index()
    
    # Keep only Date and Close price
    df = pd.DataFrame({
        'Date': brent['Date'],
        'Price': brent['Close']
    })
    
    # Remove any NaN values
    df = df.dropna()
    
    # Calculate log returns
    df['log_returns'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
    
    return df

def save_brent_data():
    """Fetch and save Brent oil data to CSV"""
    import numpy as np
    
    df = fetch_brent_oil_data()
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(data_dir, exist_ok=True)
    
    # Save to CSV
    filepath = os.path.join(data_dir, 'BrentOilPrices.csv')
    df.to_csv(filepath, index=False)
    
    print(f"Brent oil data saved to {filepath}")
    print(f"Data shape: {df.shape}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    return filepath

if __name__ == "__main__":
    save_brent_data()