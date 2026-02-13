"""
Order management module.
"""

from bot.client import BinanceFuturesClient, BinanceClientError
from bot.validators import validate_all_inputs, ValidationError
from bot.logging_config import get_logger

logger = get_logger()


class OrderManager:
    """Manages order placement and response handling."""
    
    def __init__(self, api_key, api_secret):
        """Initialize OrderManager with API credentials"""
        self.client = BinanceFuturesClient(api_key, api_secret, testnet=True)
        logger.info("OrderManager initialized")
    
    def create_order(self, symbol, side, order_type, quantity, price=None):
        """Create and place an order with validation"""
        # Validate inputs
        try:
            validated = validate_all_inputs(symbol, side, order_type, quantity, price)
        except ValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            raise
        
        # Test connection
        try:
            self.client.test_connection()
        except BinanceClientError as e:
            logger.error(f"Connection test failed: {str(e)}")
            raise
        
        # Place order
        try:
            if validated['order_type'] == 'MARKET':
                response = self.client.place_market_order(
                    symbol=validated['symbol'],
                    side=validated['side'],
                    quantity=validated['quantity']
                )
            else:  # LIMIT
                response = self.client.place_limit_order(
                    symbol=validated['symbol'],
                    side=validated['side'],
                    quantity=validated['quantity'],
                    price=validated['price']
                )
            
            logger.info(f"Order created successfully: {response.get('orderId')}")
            return response
        
        except BinanceClientError as e:
            logger.error(f"Order creation failed: {str(e)}")
            raise
    
    def format_order_summary(self, symbol, side, order_type, quantity, price=None):
        """Format order request summary for display"""
        summary = f"\n{'='*50}\n"
        summary += "ORDER REQUEST SUMMARY\n"
        summary += f"{'='*50}\n"
        summary += f"Symbol:      {symbol}\n"
        summary += f"Side:        {side}\n"
        summary += f"Type:        {order_type}\n"
        summary += f"Quantity:    {quantity}\n"
        if price:
            summary += f"Price:       {price}\n"
        summary += f"{'='*50}\n"
        return summary
    
    def format_order_response(self, response):
        """Format order response for display"""
        output = f"\n{'='*50}\n"
        output += "ORDER RESPONSE\n"
        output += f"{'='*50}\n"
        output += f"Order ID:        {response.get('orderId', 'N/A')}\n"
        output += f"Status:          {response.get('status', 'N/A')}\n"
        output += f"Symbol:          {response.get('symbol', 'N/A')}\n"
        output += f"Side:            {response.get('side', 'N/A')}\n"
        output += f"Type:            {response.get('type', 'N/A')}\n"
        output += f"Quantity:        {response.get('origQty', 'N/A')}\n"
        
        if 'executedQty' in response and float(response['executedQty']) > 0:
            output += f"Executed Qty:    {response.get('executedQty', 'N/A')}\n"
        
        if 'avgPrice' in response and float(response['avgPrice']) > 0:
            output += f"Avg Price:       {response.get('avgPrice', 'N/A')}\n"
        elif 'price' in response and response['price'] != '0':
            output += f"Limit Price:     {response.get('price', 'N/A')}\n"
        
        output += f"Update Time:     {response.get('updateTime', 'N/A')}\n"
        output += f"{'='*50}\n"
        
        if response.get('status') == 'FILLED':
            output += "✓ Order FILLED successfully!\n"
        elif response.get('status') == 'NEW':
            output += "✓ Order placed successfully! (Status: NEW)\n"
        else:
            output += f"Order status: {response.get('status', 'UNKNOWN')}\n"
        
        output += f"{'='*50}\n"
        return output