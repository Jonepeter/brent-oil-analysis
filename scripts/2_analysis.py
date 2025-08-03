"""
2_analysis.py
Bayesian change point analysis for Brent oil prices
"""

import pandas as pd
import numpy as np
import pymc as pm
import matplotlib.pyplot as plt
from pathlib import Path

def load_processed_data():
    """Load cleaned data"""
    data_path = Path(__file__).parent.parent / 'data' / 'processed' / 'brent-oil-prices_cleaned.csv'
    return pd.read_csv(data_path, parse_dates=['Date'])

def run_changepoint_analysis():
    """Execute Bayesian change point analysis"""
    df = load_processed_data()
    y = df['log_returns'].dropna().values
    n = len(y)
    
    with pm.Model() as model:
        # Change point location
        tau = pm.DiscreteUniform('tau', lower=1, upper=n-2)
        
        # Parameters before/after change point
        mu_1 = pm.Normal('mu_1', mu=0, sigma=1)
        mu_2 = pm.Normal('mu_2', mu=0, sigma=1)
        sigma_1 = pm.HalfNormal('sigma_1', sigma=1)
        sigma_2 = pm.HalfNormal('sigma_2', sigma=1)
        
        # Switch function
        idx = np.arange(n)
        mu = pm.math.switch(tau >= idx, mu_1, mu_2)
        sigma = pm.math.switch(tau >= idx, sigma_1, sigma_2)
        
        # Likelihood
        likelihood = pm.Normal('y', mu=mu, sigma=sigma, observed=y)
        
        # Sample
        trace = pm.sample(2000, tune=1000, chains=2, return_inferencedata=True)
    
    return trace, df

def save_results(trace, df):
    """Save analysis results"""
    outputs_dir = Path(__file__).parent.parent / 'outputs'
    
    # Extract change point
    tau_samples = trace.posterior['tau'].values.flatten()
    changepoint_idx = int(np.median(tau_samples))
    changepoint_date = df.iloc[changepoint_idx]['Date']
    
    # Create summary
    summary = {
        'changepoint_date': changepoint_date,
        'changepoint_index': changepoint_idx,
        'mu_1_mean': trace.posterior['mu_1'].values.mean(),
        'mu_2_mean': trace.posterior['mu_2'].values.mean(),
        'sigma_1_mean': trace.posterior['sigma_1'].values.mean(),
        'sigma_2_mean': trace.posterior['sigma_2'].values.mean()
    }
    
    # Save summary table
    pd.DataFrame([summary]).to_csv(outputs_dir / 'tables' / 'changepoint_summary.csv', index=False)
    
    print(f"✅ Analysis complete")
    print(f"📍 Change point detected: {changepoint_date}")
    
    return summary

if __name__ == "__main__":
    trace, df = run_changepoint_analysis()
    summary = save_results(trace, df)