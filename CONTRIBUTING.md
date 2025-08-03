# Contributing to Brent Oil Analysis

## Development Environment
- **OS**: Windows 11
- **Python**: 3.13.1
- **Package Manager**: pip

## Git Workflow

### Branch Strategy
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature branches

### Development Process

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd brent-oil-analysis
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Create Feature Branch**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

3. **Development**
   ```bash
   # Make changes
   git add .
   git commit -m "feat: add your feature description"
   ```

4. **Push and PR**
   ```bash
   git push origin feature/your-feature-name
   # Create Pull Request to develop branch
   ```

### Commit Convention
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation updates
- `refactor:` Code refactoring
- `test:` Adding tests

### Before Committing
```bash
# Run tests
python -m pytest tests/

# Check code quality
python src/data_fetcher.py
```