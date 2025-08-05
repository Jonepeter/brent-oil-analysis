# This script fetches historical Brent oil price data from Yahoo Finance,
# computes log returns, and saves both raw and cleaned versions of the data
# to the appropriate directories for further analysis.

import yfinance as yf
import pandas as pd
import numpy as np
from pathlib import Path


def main():
    # Setup paths for raw and processed data directories
    base_path = Path(__file__).parent.parent
    raw_dir = base_path / "data" / "raw"
    processed_dir = base_path / "data" / "processed"

    # Fetch Brent oil data from Yahoo Finance (from 1987-05-20 to 2024-12-31)
    brent = yf.download("BZ=F", start="1987-05-20", end="2024-12-31")
    df = (
        pd.DataFrame({"Date": brent.index, "Price": brent["Close"]})
        .dropna()
        .reset_index(drop=True)
    )

    # Calculate log returns of the price series
    df["log_returns"] = np.log(df["Price"]).diff()

    # Save the raw and cleaned data to CSV files
    df.to_csv(raw_dir / "brent-oil-prices_raw.csv", index=False)
    df.to_csv(processed_dir / "brent-oil-prices_cleaned.csv", index=False)

    print(
        f"Processed {len(df)} observations ({df['Date'].min()} to {df['Date'].max()})"
    )


if __name__ == "__main__":
    main()
