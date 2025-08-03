import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from scipy import stats

class TimeSeriesAnalyzer:
    def __init__(self, data):
        self.data = data
        
    def check_stationarity(self, column='Price', alpha=0.05):
        """Perform Augmented Dickey-Fuller test for stationarity"""
        result = adfuller(self.data[column].dropna())
        
        return {
            'adf_statistic': result[0],
            'p_value': result[1],
            'critical_values': result[4],
            'is_stationary': result[1] < alpha
        }
    
    def plot_price_series(self, figsize=(15, 8)):
        """Plot price series with trend analysis"""
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # Price over time
        axes[0,0].plot(self.data['Date'], self.data['Price'])
        axes[0,0].set_title('Brent Oil Prices Over Time')
        axes[0,0].set_ylabel('Price (USD/barrel)')
        
        # Log returns
        axes[0,1].plot(self.data['Date'], self.data['log_returns'])
        axes[0,1].set_title('Log Returns')
        axes[0,1].set_ylabel('Log Returns')
        
        # Price distribution
        axes[1,0].hist(self.data['Price'], bins=50, alpha=0.7)
        axes[1,0].set_title('Price Distribution')
        axes[1,0].set_xlabel('Price (USD/barrel)')
        
        # Log returns distribution
        axes[1,1].hist(self.data['log_returns'].dropna(), bins=50, alpha=0.7)
        axes[1,1].set_title('Log Returns Distribution')
        axes[1,1].set_xlabel('Log Returns')
        
        plt.tight_layout()
        return fig
    
    def volatility_analysis(self, window=30):
        """Calculate rolling volatility"""
        self.data[f'volatility_{window}d'] = self.data['log_returns'].rolling(window=window).std()
        return self.data[f'volatility_{window}d']
    
    def detect_outliers(self, column='log_returns', threshold=3):
        """Detect outliers using z-score"""
        z_scores = np.abs(stats.zscore(self.data[column].dropna()))
        outliers = self.data[z_scores > threshold]
        return outliers