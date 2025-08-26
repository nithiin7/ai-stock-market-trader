#!/usr/bin/env python3
"""
Main entry point for the AI Stock Trader system.
"""

import asyncio
import sys
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

from ai_stock_trader.web.app import main
from ai_stock_trader.core.trading_floor import TradingFloor


async def run_trading_floor():
    """Run the trading floor system."""
    trading_floor = TradingFloor()
    await trading_floor.run()


def run_web_app():
    """Run the web application."""
    main()


def main_cli():
    """Main CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Stock Market Trader")
    parser.add_argument(
        "--mode",
        choices=["web", "trading"],
        default="web",
        help="Run mode: web (Gradio interface) or trading (trading floor)"
    )
    
    args = parser.parse_args()
    
    if args.mode == "web":
        run_web_app()
    elif args.mode == "trading":
        asyncio.run(run_trading_floor())


if __name__ == "__main__":
    main_cli()
