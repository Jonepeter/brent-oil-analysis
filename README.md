# Brent Oil Price Change Point Analysis

## Business Objective

Study how important events affect Brent oil prices by detecting changes and associating causes on time series data. Focus on political decisions, conflicts, sanctions, and OPEC policy changes to provide insights for investors, analysts, and policymakers.

## Project Structure

```bash
brent-oil-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── analysis/
│   ├── models/
│   └── utils/
├── notebooks/
├── dashboard/
│   ├── backend/
│   └── frontend/
├── reports/
└── requirements.txt
```

## Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd brent-oil-analysis
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up data directories**

   ```bash
   mkdir -p data/raw data/processed reports
   ```

### Running the Analysis

1. **Execute notebooks in sequence**
   - Start with data collection and preprocessing notebooks
   - Run change point detection analysis
   - Generate reports and visualizations

2. **Launch the dashboard**

```bash
   cd dashboard/backend
   python app.py
   ```

Access the dashboard at `http://localhost:5000`

### Configuration

- Update data sources in `src/utils/config.py`
- Modify analysis parameters in notebook configurations
- Customize dashboard settings in `dashboard/backend/config.py`

## Key Components

- Bayesian Change Point Detection using PyMC3
- Event correlation analysis
- Interactive dashboard with Flask/React
- Statistical validation and insights
