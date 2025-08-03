import pandas as pd
import numpy as np
from datetime import datetime

def load_brent_data(filepath):
    """Load and preprocess Brent oil price data"""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    df = df.sort_values('Date').reset_index(drop=True)
    df['log_returns'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
    return df

def load_events_data(filepath):
    """Load events data"""
    events_df = pd.read_csv(filepath)
    events_df['Date'] = pd.to_datetime(events_df['Date'])
    return events_df

def prepare_analysis_data(price_df, start_date=None, end_date=None):
    """Prepare data for change point analysis"""
    if start_date:
        price_df = price_df[price_df['Date'] >= start_date]
    if end_date:
        price_df = price_df[price_df['Date'] <= end_date]
    
    price_df = price_df.dropna()
    price_df['days_since_start'] = (price_df['Date'] - price_df['Date'].min()).dt.days
    return price_df