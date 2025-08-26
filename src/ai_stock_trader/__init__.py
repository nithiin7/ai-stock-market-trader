"""
AI Stock Market Trader

An AI-powered stock market trading system built using OpenAI Agents SDK.
"""

__version__ = "0.1.0"
__author__ = "AI Stock Trader Team"

# Import only the safe modules initially
from .accounts.account import Account
from .market.market_data import get_share_price
from .utils.database import write_account, read_account
from .utils.helpers import Color
from .config.settings import get_settings
from .utils.logging import get_logger

__all__ = [
    "Account",
    "get_share_price",
    "write_account", 
    "read_account",
    "Color",
    "get_settings",
    "get_logger",
]

# Lazy imports for modules that depend on the agents package
def get_trader():
    """Get the Trader class (lazy import to avoid agents package issues)."""
    from .core.trader import Trader
    return Trader

def get_trading_floor():
    """Get the TradingFloor class (lazy import to avoid agents package issues)."""
    from .core.trading_floor import TradingFloor
    return TradingFloor
