#!/usr/bin/env python3
"""
Trading Bot CLI - Command Line Interface for Binance Futures Testnet
"""

import argparse
import sys
from bot.orders import OrderManager
from bot.validators import ValidationError
from bot.client import BinanceClientError
from bot.logging_config import setup_logging, get_logger

# Import config
try:
    import config
except ImportError:
    print("\n" + "="*60)
    print("ERROR: config.py file not found!")
    print("="*60)
    print("\nPlease create a config.py file with your API credentials:")
    print("1. Copy config_template.py to config.py")
    print("2. Add your Binance Futures Testnet API key and secret")
    print("3. Get credentials from: https://testnet.binancefuture.com")
    print("="*60 + "\n")
    sys.exit(1)


def main():
    """Main CLI entry point"""
    
    # Set up logging
    setup_logging()
    logger = get_logger()
    
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Trading Bot - Place orders on Binance Futures Testnet'
    )
    
    # Add arguments
    parser.add_argument('--symbol', type=str, required=True,
                        help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', type=str, required=True,
                        choices=['BUY', 'SELL', 'buy', 'sell'],
                        help='Order side: BUY or SELL')
    parser.add_argument('--type', type=str, required=True,
                        choices=['MARKET', 'LIMIT', 'market', 'limit'],
                        help='Order type: MARKET or LIMIT')
    parser.add_argument('--quantity', type=float, required=True,
                        help='Order quantity')
    parser.add_argument('--price', type=float, required=False,
                        help='Limit price (required for LIMIT orders)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Print header
    print("\n" + "="*60)
    print("BINANCE FUTURES TESTNET - TRADING BOT")
    print("="*60)
    
    try:
        # Initialize order manager
        logger.info("Initializing Trading Bot...")
        order_manager = OrderManager(config.API_KEY, config.API_SECRET)
        
        # Print order summary
        summary = order_manager.format_order_summary(
            symbol=args.symbol,
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )
        print(summary)
        
        # Ask for confirmation
        confirm = input("Proceed with order? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print("\nOrder cancelled by user.")
            logger.info("Order cancelled by user")
            sys.exit(0)
        
        # Create order
        logger.info("Placing order...")
        response = order_manager.create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        # Print response
        output = order_manager.format_order_response(response)
        print(output)
        
        logger.info("Order completed successfully")
        sys.exit(0)
    
    except ValidationError as e:
        print(f"\n❌ VALIDATION ERROR: {str(e)}\n")
        logger.error(f"Validation error: {str(e)}")
        sys.exit(1)
    
    except BinanceClientError as e:
        print(f"\n❌ API ERROR: {str(e)}\n")
        logger.error(f"API error: {str(e)}")
        sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.\n")
        logger.info("Operation cancelled by user")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {str(e)}\n")
        logger.exception("Unexpected error occurred")
        sys.exit(1)


if __name__ == '__main__':
    main()