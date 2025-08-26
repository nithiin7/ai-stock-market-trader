#!/usr/bin/env python3
"""
Basic import test for AI Stock Trader.
"""

import sys
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def test_basic_imports():
    """Test basic imports without the problematic agents package."""
    try:
        print("Testing basic imports...")
        
        # Test core modules
        from ai_stock_trader.accounts.account import Account, Transaction
        print("✓ Account and Transaction imported successfully")
        
        from ai_stock_trader.market.market_data import get_share_price
        print("✓ Market data functions imported successfully")
        
        from ai_stock_trader.utils.database import write_account, read_account
        print("✓ Database functions imported successfully")
        
        from ai_stock_trader.utils.helpers import Color
        print("✓ Helper utilities imported successfully")
        
        from ai_stock_trader.config.settings import get_settings
        print("✓ Configuration settings imported successfully")
        
        from ai_stock_trader.utils.logging import get_logger
        print("✓ Logging utilities imported successfully")
        
        print("\n✅ All basic imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_basic_imports()
