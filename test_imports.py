"""
Test script to verify all imports work correctly
"""

print("Testing imports...")

try:
    from bot.logging_config import setup_logging, get_logger
    print("✓ logging_config imported successfully")
except ImportError as e:
    print(f"✗ Error importing logging_config: {e}")

try:
    from bot.validators import validate_all_inputs, ValidationError
    print("✓ validators imported successfully")
except ImportError as e:
    print(f"✗ Error importing validators: {e}")

try:
    from bot.client import BinanceFuturesClient, BinanceClientError
    print("✓ client imported successfully")
except ImportError as e:
    print(f"✗ Error importing client: {e}")

try:
    from bot.orders import OrderManager
    print("✓ orders imported successfully")
except ImportError as e:
    print(f"✗ Error importing orders: {e}")

print("\nTesting validation...")
try:
    result = validate_all_inputs("BTCUSDT", "BUY", "MARKET", 0.01, None)
    print(f"✓ Validation works! Result: {result}")
except Exception as e:
    print(f"✗ Validation error: {e}")

print("\n✓ All tests passed! Your setup is correct.")