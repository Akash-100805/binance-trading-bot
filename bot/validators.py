"""
Input validation module for trading bot.
"""

import re
from bot.logging_config import get_logger

logger = get_logger()


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_symbol(symbol):
    """Validate trading symbol format (e.g., BTCUSDT)"""
    if not symbol:
        raise ValidationError("Symbol cannot be empty")
    
    symbol = symbol.upper()
    
    if not re.match(r'^[A-Z0-9]+$', symbol):
        raise ValidationError(f"Invalid symbol format: {symbol}")
    
    if len(symbol) < 6:
        raise ValidationError(f"Symbol too short: {symbol}")
    
    logger.debug(f"Symbol validated: {symbol}")
    return symbol


def validate_side(side):
    """Validate order side (BUY or SELL)"""
    if not side:
        raise ValidationError("Side cannot be empty")
    
    side = side.upper()
    
    if side not in ['BUY', 'SELL']:
        raise ValidationError(f"Invalid side: {side}. Must be BUY or SELL")
    
    logger.debug(f"Side validated: {side}")
    return side


def validate_order_type(order_type):
    """Validate order type (MARKET or LIMIT)"""
    if not order_type:
        raise ValidationError("Order type cannot be empty")
    
    order_type = order_type.upper()
    
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValidationError(f"Invalid order type: {order_type}. Must be MARKET or LIMIT")
    
    logger.debug(f"Order type validated: {order_type}")
    return order_type


def validate_quantity(quantity):
    """Validate order quantity"""
    try:
        qty = float(quantity)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid quantity format: {quantity}")
    
    if qty <= 0:
        raise ValidationError(f"Quantity must be positive: {qty}")
    
    logger.debug(f"Quantity validated: {qty}")
    return qty


def validate_price(price, order_type):
    """Validate order price (required for LIMIT orders)"""
    # Price not needed for MARKET orders
    if order_type == 'MARKET':
        return None
    
    # Price required for LIMIT orders
    if price is None:
        raise ValidationError("Price is required for LIMIT orders")
    
    try:
        p = float(price)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid price format: {price}")
    
    if p <= 0:
        raise ValidationError(f"Price must be positive: {p}")
    
    logger.debug(f"Price validated: {p}")
    return p


def validate_all_inputs(symbol, side, order_type, quantity, price=None):
    """Validate all inputs at once"""
    validated = {}
    
    validated['symbol'] = validate_symbol(symbol)
    validated['side'] = validate_side(side)
    validated['order_type'] = validate_order_type(order_type)
    validated['quantity'] = validate_quantity(quantity)
    validated['price'] = validate_price(price, validated['order_type'])
    
    logger.info(f"All inputs validated successfully: {validated}")
    return validated    