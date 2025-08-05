import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from scipy import stats


class TimeSeriesAnalyzer:
    """
    A class for performing basic time series analysis on financial data, such as Brent oil prices.

    Methods
    -------
    check_stationarity(column='Price', alpha=0.05):
        Performs the Augmented Dickey-Fuller test to check for stationarity in the specified column.
    plot_price_series(figsize=(15, 8)):
        Plots the price series, log returns, and their distributions.
    volatility_analysis(window=30):
        Calculates rolling volatility (standard deviation of log returns) over a specified window.
    detect_outliers(column='log_returns', threshold=3):
        Detects outliers in the specified column using the z-score method.
    """

    def __init__(self, data):
        """
        Initialize the TimeSeriesAnalyzer with a pandas DataFrame.

        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing at least 'Date', 'Price', and 'log_returns' columns.
        """
        self.data = data

    def check_stationarity(self, column="Price", alpha=0.05):
        """
        Perform Augmented Dickey-Fuller test for stationarity on a given column.

        Parameters
        ----------
        column : str, optional
            The column to test for stationarity (default is 'Price').
        alpha : float, optional
            Significance level for the test (default is 0.05).

        Returns
        -------
        dict
            Dictionary containing ADF statistic, p-value, critical values, and stationarity boolean.
        """
        # Drop missing values and run the ADF test
        result = adfuller(self.data[column].dropna())

        return {
            "adf_statistic": result[0],
            "p_value": result[1],
            "critical_values": result[4],
            "is_stationary": result[1] < alpha,
        }

    def plot_price_series(self, figsize=(15, 8)):
        """
        Plot price series, log returns, and their distributions.

        Parameters
        ----------
        figsize : tuple, optional
            Size of the matplotlib figure (default is (15, 8)).

        Returns
        -------
        matplotlib.figure.Figure
            The matplotlib figure object containing the plots.
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)

        # Plot price over time
        axes[0, 0].plot(self.data["Date"], self.data["Price"])
        axes[0, 0].set_title("Brent Oil Prices Over Time")
        axes[0, 0].set_ylabel("Price (USD/barrel)")

        # Plot log returns over time
        axes[0, 1].plot(self.data["Date"], self.data["log_returns"])
        axes[0, 1].set_title("Log Returns")
        axes[0, 1].set_ylabel("Log Returns")

        # Plot price distribution
        axes[1, 0].hist(self.data["Price"], bins=50, alpha=0.7)
        axes[1, 0].set_title("Price Distribution")
        axes[1, 0].set_xlabel("Price (USD/barrel)")

        # Plot log returns distribution
        axes[1, 1].hist(self.data["log_returns"].dropna(), bins=50, alpha=0.7)
        axes[1, 1].set_title("Log Returns Distribution")
        axes[1, 1].set_xlabel("Log Returns")

        plt.tight_layout()
        return fig

    def volatility_analysis(self, window=30):
        """
        Calculate rolling volatility (standard deviation of log returns) over a specified window.

        Parameters
        ----------
        window : int, optional
            The rolling window size in days (default is 30).

        Returns
        -------
        pd.Series
            Series containing the rolling volatility.
        """
        # Calculate rolling standard deviation of log returns
        self.data[f"volatility_{window}d"] = (
            self.data["log_returns"].rolling(window=window).std()
        )
        return self.data[f"volatility_{window}d"]

    def detect_outliers(self, column="log_returns", threshold=3):
        """
        Detect outliers in a column using the z-score method.

        Parameters
        ----------
        column : str, optional
            The column to check for outliers (default is 'log_returns').
        threshold : float, optional
            The z-score threshold to identify outliers (default is 3).

        Returns
        -------
        pd.DataFrame
            DataFrame containing the outlier rows.
        """
        # Compute z-scores for the specified column, ignoring NaNs
        z_scores = np.abs(stats.zscore(self.data[column].dropna()))
        # Select rows where z-score exceeds the threshold
        outliers = self.data[z_scores > threshold]
        return outliers
