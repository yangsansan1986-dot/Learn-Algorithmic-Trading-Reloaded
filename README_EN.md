# Learn Algorithmic Trading - Reloaded

This project is a modified and optimized version of the code accompanying the book "Learn Algorithmic Trading".

## Project Overview

This codebase contains implementations of core concepts in algorithmic trading, covering the complete workflow from technical indicator calculation to strategy backtesting. The original book code had several compatibility issues and logical errors, which have been fixed and improved in this version.

**Original Book Code Repository**: [https://github.com/PacktPublishing/Learn-Algorithmic-Trading](https://github.com/PacktPublishing/Learn-Algorithmic-Trading)

## Key Modifications

### 1. Chapter 5 - Statistical Arbitrage Strategy
- Fixed mathematical logic errors in covariance calculation in `stat_arb.py`
- Corrected logical issues in PnL (Profit and Loss) calculation
- Optimized the calculation method for open positions

### 2. Chapter 7 - Trading Simulation Framework
- Fixed import issues in unit test files (`ModuleNotFoundError: No module named 'chapter7'`)
- Changed absolute imports to relative imports for proper module loading

### 3. Chapter 8 - FIX Protocol Simulator
- Fixed `quickfix.Exception` compatibility issue, changed to `quickfix.FIXException`
- Fixed module import path issue (`from sim import ...` → `from fixsim.sim import ...`)
- Fixed `yaml.load()` security warning by adding `Loader=yaml.SafeLoader` parameter

### 4. Chapter 9 - Data Storage & Strategy Implementation
- **hd5pandareader.py**: Fixed pandas `to_hdf()` API compatibility (added `key=` parameter)
- **hd5pandareader.py**: Created simulated financial data to replace Yahoo Finance data source (original source no longer available)
- **kdb_data.py**: Replaced pyq/KDB+ database dependency with pandas DataFrame (avoids complex KDB+ installation)
- **TradingStrategyDualMA.py**: Identified and flagged duplicate `handle_book_event` call issue

## Python Version & Dependencies

### Python Version
- Python 3.12

### Core Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| pandas | 3.0.2 | Data analysis and processing |
| numpy | 2.4.4 | Numerical computation |
| matplotlib | 3.10.8 | Data visualization |
| scikit-learn | 1.5.0 | Machine learning algorithms |
| quickfix | 1.15.1 | FIX protocol implementation |
| h5py | 3.16.0 | HDF5 data storage |
| tables | 3.11.1 | High-performance HDF5 data processing |
| twisted | 24.3.0 | Asynchronous network programming |
| pyyaml | 6.0.3 | YAML configuration file processing |
| pandas-datareader | 0.10.0 | Financial data retrieval |

### Install Dependencies

```bash
# Install all dependencies using pip
pip install -r requirements.txt

# Or use virtual environment
e:\Code\python\Learn\py312\Scripts\pip.exe install -r requirements.txt
```

## Project Structure

```
Learn-Algorithmic-Trading-Reloaded/
├── Chapter1/              # Basic concepts
├── Chapter2/              # Technical indicators (SMA, EMA, MACD, RSI, etc.)
├── Chapter3/              # Machine learning models (KNN, Logistic, SVM, etc.)
├── Chapter4/              # Trading strategies (Dual MA, Turtle Trading, etc.)
├── Chapter5/              # Statistical arbitrage strategies
├── Chapter6/              # Risk management
├── Chapter7/              # Trading simulation framework
├── Chapter8/              # FIX protocol simulator
└── Chapter9/              # Data storage & event-driven backtesting
```

## Usage

### Run FIX Simulator

```bash
# Start FIX Server
cd Chapter8/fixsim
python fixsim-server.py -ac fixsim-server.conf.ini -c fixsim-server.conf.yaml

# Start FIX Client (in new terminal)
cd Chapter8/fixsim
python fixsim-client.py -ic fixsim-client.conf.ini -c fixsim-client.conf.yaml
```

### Run HDF5 Example

```bash
cd Chapter9
python hd5pandareader.py
```

### Run KDB+ Alternative Example

```bash
cd Chapter9
python kdb_data.py
```

## Notes

1. **Yahoo Finance Data Source**: The original Yahoo Finance API used in the book is no longer available, simulated data is used in some code
2. **KDB+ Database**: `kdb_data.py` has been implemented using pandas instead, no KDB+ installation required
3. **quickfix Installation**: The quickfix package requires a C++ compilation environment, precompiled versions are recommended

## License

MIT License
