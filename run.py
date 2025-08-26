#!/usr/bin/env python3
"""
Simple run script for AI Stock Trader.
"""

import sys
import os
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def main():
    """Main entry point."""
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
        print("Starting AI Stock Trader Web Interface...")
        from ai_stock_trader.web.app import main as web_main
        web_main()
    elif args.mode == "trading":
        print("Starting AI Stock Trader Trading Floor...")
        import asyncio
        from ai_stock_trader.core.trading_floor import TradingFloor
        
        async def run_trading():
            trading_floor = TradingFloor()
            await trading_floor.run()
        
        asyncio.run(run_trading())

if __name__ == "__main__":
    main()
