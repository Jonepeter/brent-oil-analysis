# 🛢️ Brent Oil Price Change Point Analysis

[![CI/CD Pipeline](https://github.com/yourusername/brent-oil-analysis/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/yourusername/brent-oil-analysis/actions)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)

## 🎯 Business Objective

Detect structural breaks in Brent oil prices using Bayesian change point analysis and correlate them with major geopolitical events. Provides actionable insights for investors, analysts, and policymakers.

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/brent-oil-analysis.git
cd brent-oil-analysis
```

### 2. Setup Environment
**Option A: pip**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

**Option B: conda**
```bash
conda env create -f environment.yml
conda activate brent-oil
```

### 3. Run Analysis
```bash
# Process data
python scripts/1_data_processing.py

# Run change point analysis
python scripts/2_analysis.py

# Launch dashboard
cd dashboard/backend && python app.py
```

## 📂 Project Structure

| Folder | Contents |
|--------|----------|
| `data/` | Raw and processed datasets |
| `scripts/` | Executable analysis scripts |
| `notebooks/` | Exploratory Jupyter notebooks |
| `outputs/` | Generated figures and tables |
| `docs/` | Methodology and references |
| `dashboard/` | Interactive web application |
| `tests/` | Unit tests |

## 🔄 Reproduction Steps

### Step 1: Data Processing
```bash
python scripts/1_data_processing.py
```
**Output**: Clean datasets in `data/processed/`

### Step 2: Analysis
```bash
python scripts/2_analysis.py
```
**Output**: Change point results in `outputs/tables/`

### Step 3: Visualization
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```
**Output**: Plots saved to `outputs/figures/`

### Step 4: Dashboard
```bash
cd dashboard/backend && python app.py
```
**Access**: http://localhost:5000

## 📊 Key Results

- **Primary Change Point**: [Date from analysis]
- **Statistical Significance**: 95% confidence
- **Associated Events**: Major geopolitical disruptions
- **Impact Magnitude**: Quantified regime shifts

## 🛠️ Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow and coding standards.

### Running Tests
```bash
python -m pytest tests/ -v
```

## 📖 Documentation

- [Methodology](docs/methodology.md) - Technical approach
- [References](docs/references.md) - Data sources and literature
- [Interim Report](reports/interim_report.md) - Detailed analysis

## 🔧 Technical Stack

- **Analysis**: PyMC (Bayesian modeling), pandas, NumPy
- **Visualization**: matplotlib, seaborn
- **Dashboard**: Flask (backend), React (frontend)
- **Testing**: pytest
- **CI/CD**: GitHub Actions

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👥 Contributors

- **Lead Analyst**: [Your Name]
- **Data Science Team**: 10 Academy Week 10 Project

---

*For questions or issues, please open a GitHub issue or contact the development team.*