# Trading Bot - Binance Futures Testnet

A command-line trading bot for placing orders on Binance Futures Testnet.

## Features

- Place MARKET and LIMIT orders
- Support for BUY and SELL sides
- Input validation with clear error messages
- Comprehensive logging of all operations
- Clean, modular code structure
- Proper error handling

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get API Credentials

1. Go to https://testnet.binancefuture.com
2. Register for a testnet account
3. Generate API Key and Secret
4. Save these credentials

### 3. Configure API Keys
```bash
# Copy the template
cp config_template.py config.py

# Edit config.py and add your credentials
```

Edit `config.py`:
```python
API_KEY = "your_actual_api_key_here"
API_SECRET = "your_actual_api_secret_here"
```

## Usage

### MARKET Order Examples
```bash
# BUY order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# SELL order
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.1
```

### LIMIT Order Examples
```bash
# BUY order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 45000

# SELL order
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.1 --price 3500
```

## Command-Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--symbol` | Yes | Trading pair (e.g., BTCUSDT) |
| `--side` | Yes | BUY or SELL |
| `--type` | Yes | MARKET or LIMIT |
| `--quantity` | Yes | Order quantity |
| `--price` | For LIMIT | Price for limit orders |

## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order management
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
├── cli.py                 # CLI interface
├── config_template.py     # Config template
├── requirements.txt       # Dependencies
├── .gitignore
└── README.md
```

## Logging

All operations are logged to `logs/` directory with timestamp:
- API requests and responses
- Order details
- Errors and exceptions

## Error Handling

The bot handles:
- Invalid inputs
- API errors
- Network failures
- Missing configuration

## Security

- Never commit `config.py` (it's in .gitignore)
- Use testnet credentials only
- Keep API keys secure

## Requirements

- Python 3.7+
- Internet connection
- Binance Futures Testnet account