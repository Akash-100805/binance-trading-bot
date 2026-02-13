# Trading Bot - Binance Futures Testnet

A command-line trading bot for placing orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET and LIMIT orders
- Support for BUY and SELL sides
- Input validation with error handling
- Comprehensive logging
- Clean, modular code structure

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get API Credentials

1. Go to https://testnet.binancefuture.com
2. Register and generate API keys
3. Copy `config_template.py` to `config.py`
4. Add your API credentials to `config.py`

### 3. Usage

**MARKET Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

**LIMIT Order:**
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000
```

## Project Structure
```
trading_bot/
├── bot/
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order management
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
├── cli.py                 # CLI interface
├── config_template.py     # API credentials template
├── requirements.txt       # Dependencies
└── README.md
```

## Requirements

- Python 3.7+
- Binance Futures Testnet account
- Internet connection

## Logging

All operations are logged to `logs/` directory with timestamps.
