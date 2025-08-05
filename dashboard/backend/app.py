from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

app = Flask(__name__)
CORS(app)

def load_brent_data():
    """Load real Brent oil data"""
    try:
        # Try to load existing data
        data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw', 'BrentOilPrices.csv')
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
            df['Date'] = pd.to_datetime(df['Date'], format='mixed')
            df = df.sort_values('Date').reset_index(drop=True)
            df['log_returns'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
            return df
        else:
            # Fetch new data
            print("No existing data found. Fetching new data...")
    except Exception as e:
        print(f"Error loading real data: {e}")
        # Fallback to sample data
        # return load_sample_data()

def load_sample_data():
    """Generate sample data as fallback"""
    np.random.seed(42)
    dates = pd.date_range('2000-01-01', '2022-12-31', freq='D')
    n = len(dates)
    changepoint = n // 2
    
    returns_1 = np.random.normal(0.001, 0.02, changepoint)
    returns_2 = np.random.normal(-0.0005, 0.03, n - changepoint)
    log_returns = np.concatenate([returns_1, returns_2])
    
    prices = [100]
    for ret in log_returns:
        prices.append(prices[-1] * np.exp(ret))
    
    return pd.DataFrame({
        'Date': dates,
        'Price': prices[1:],
        'log_returns': log_returns
    })

def load_events():
    """Load events data"""
    events_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'events_data.csv')
    return pd.read_csv(events_path)

# Global data
price_data = load_brent_data()
events_data = load_events()
events_data['Date'] = pd.to_datetime(events_data['Date'])

@app.route('/')
def index():
    return "Welcome to the Brent Oil API"

@app.route('/api/price-data')
def get_price_data():
    """Get price data for visualization"""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    df = price_data.copy()
    if start_date:
        df = df[df['Date'] >= start_date]
    if end_date:
        df = df[df['Date'] <= end_date]
    
    return jsonify({
        'dates': df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        'prices': df['Price'].fillna(0).tolist(),
        'returns': df['log_returns'].fillna(0).tolist()
    })

@app.route('/api/events')
def get_events():
    """Get events data"""
    return jsonify({
        'events': events_data.to_dict('records')
    })

@app.route('/api/changepoints')
def get_changepoints():
    """Get detected change points"""
    # Simulated change point results
    changepoint_date = price_data['Date'].iloc[len(price_data) // 2]
    
    return jsonify({
        'changepoints': [{
            'date': changepoint_date.strftime('%Y-%m-%d'),
            'confidence': 0.95,
            'impact': {
                'price_change_pct': 15.2,
                'volatility_change_pct': 25.8
            }
        }]
    })

@app.route('/api/analysis-summary')
def get_analysis_summary():
    """Get analysis summary statistics"""
    return jsonify({
        'total_observations': len(price_data),
        'date_range': {
            'start': price_data['Date'].min().strftime('%Y-%m-%d'),
            'end': price_data['Date'].max().strftime('%Y-%m-%d')
        },
        'price_stats': {
            'mean': float(price_data['Price'].mean()),
            'std': float(price_data['Price'].std()),
            'min': float(price_data['Price'].min()),
            'max': float(price_data['Price'].max())
        },
        'total_events': len(events_data),
        'changepoints_detected': 1
    })

@app.route('/api/event-impact/<event_id>')
def get_event_impact(event_id):
    """Get impact analysis for specific event"""
    event_idx = int(event_id)
    if event_idx >= len(events_data):
        return jsonify({'error': 'Event not found'}), 404
    
    event = events_data.iloc[event_idx]
    event_date = pd.to_datetime(event['Date'])
    
    # Calculate price impact around event
    window = 10
    before_data = price_data[
        (price_data['Date'] >= event_date - timedelta(days=window)) &
        (price_data['Date'] < event_date)
    ]
    after_data = price_data[
        (price_data['Date'] >= event_date) &
        (price_data['Date'] <= event_date + timedelta(days=window))
    ]
    
    if len(before_data) > 0 and len(after_data) > 0:
        price_change = ((after_data['Price'].mean() - before_data['Price'].mean()) / 
                       before_data['Price'].mean() * 100)
        volatility_change = ((after_data['log_returns'].std() - before_data['log_returns'].std()) /
                           before_data['log_returns'].std() * 100)
    else:
        price_change = 0
        volatility_change = 0
    
    return jsonify({
        'event': event.to_dict(),
        'impact': {
            'price_change_pct': float(price_change),
            'volatility_change_pct': float(volatility_change),
            'analysis_window_days': window
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)