"""
Binance Futures Testnet API client wrapper.
"""

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import get_logger

logger = get_logger()


class BinanceClientError(Exception):
    """Custom exception for Binance client errors."""
    pass


class BinanceFuturesClient:
    """Wrapper for Binance Futures Testnet API client."""
    
    def __init__(self, api_key, api_secret, testnet=True):
        """Initialize Binance Futures client"""
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            logger.info("Binance Futures client initialized successfully")
            logger.info(f"Using {'TESTNET' if testnet else 'MAINNET'} environment")
        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {str(e)}")
            raise BinanceClientError(f"Client initialization failed: {str(e)}")
    
    def test_connection(self):
        """Test API connection and credentials"""
        try:
            # Test connectivity
            self.client.futures_ping()
            logger.info("API connectivity test successful")
            
            # Test authentication
            self.client.futures_account()
            logger.info("API authentication successful")
            
            return True
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise BinanceClientError(f"API error: {e.message}")
        except BinanceRequestException as e:
            logger.error(f"Network error: {str(e)}")
            raise BinanceClientError(f"Network error: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise BinanceClientError(f"Connection test failed: {str(e)}")
    
    def place_market_order(self, symbol, side, quantity):
        """Place a market order"""
        try:
            logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")
            
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            
            logger.info(f"MARKET order placed successfully. OrderId: {order.get('orderId')}")
            logger.debug(f"Order response: {order}")
            
            return order
        
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise BinanceClientError(f"API error: {e.message}")
        except BinanceRequestException as e:
            logger.error(f"Network error: {str(e)}")
            raise BinanceClientError(f"Network error: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise BinanceClientError(f"Order placement failed: {str(e)}")
    
    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order"""
        try:
            logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")
            
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            
            logger.info(f"LIMIT order placed successfully. OrderId: {order.get('orderId')}")
            logger.debug(f"Order response: {order}")
            
            return order
        
        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise BinanceClientError(f"API error: {e.message}")
        except BinanceRequestException as e:
            logger.error(f"Network error: {str(e)}")
            raise BinanceClientError(f"Network error: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise BinanceClientError(f"Order placement failed: {str(e)}")