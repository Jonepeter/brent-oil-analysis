# Setup Instructions

## Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

## Backend Setup

1. **Create virtual environment:**
```bash
cd brent-oil-analysis
python -m venv venv
venv\Scripts\activate  # Windows
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run Flask backend:**
```bash
cd dashboard/backend
python app.py
```
Backend will run on http://localhost:5000

## Frontend Setup

1. **Install Node dependencies:**
```bash
cd dashboard/frontend
npm install
```

2. **Start React development server:**
```bash
npm start
```
Frontend will run on http://localhost:3000

## Data Setup

1. **Add your Brent oil data:**
   - Place your CSV file in `data/raw/`
   - Update the file path in `src/utils/data_loader.py`

2. **Customize events:**
   - Edit `data/events_data.csv` to add/modify events
   - Follow the existing format

## Running Analysis

1. **Start Jupyter:**
```bash
jupyter notebook
```

2. **Run notebooks in order:**
   - `01_data_exploration.ipynb`
   - `02_changepoint_analysis.ipynb`

## Project Structure
```
brent-oil-analysis/
├── data/                    # Data files
├── src/                     # Python source code
│   ├── analysis/           # Analysis modules
│   ├── models/             # Model implementations
│   └── utils/              # Utility functions
├── notebooks/              # Jupyter notebooks
├── dashboard/              # Web dashboard
│   ├── backend/           # Flask API
│   └── frontend/          # React app
├── reports/               # Analysis reports
└── requirements.txt       # Python dependencies
```

## Troubleshooting

### Common Issues:
1. **PyMC3 installation**: May require specific Theano version
2. **React build errors**: Clear node_modules and reinstall
3. **CORS issues**: Ensure Flask-CORS is properly configured

### Environment Variables:
Create `.env` file in backend directory if needed:
```
FLASK_ENV=development
FLASK_DEBUG=True
```