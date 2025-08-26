# AI Stock Market Trader

An AI-powered stock market trading system built using OpenAI Agents SDK, designed for automated trading with intelligent decision-making capabilities.

## 🚀 Features

- **AI-Powered Trading**: Uses OpenAI Agents SDK for intelligent trading decisions
- **Multi-Model Support**: Supports various AI models (GPT-4, DeepSeek, Grok, Gemini)
- **Real-time Market Data**: Integrates with Polygon API for live market data
- **Portfolio Management**: Comprehensive account and portfolio tracking
- **Web Interface**: Beautiful Gradio-based web interface for monitoring and control
- **MCP Integration**: Model Context Protocol support for enhanced AI capabilities
- **Automated Trading**: Configurable trading strategies and automated execution

## 📁 Project Structure

```
ai-stock-market-trader/
├── src/
│   └── ai_stock_trader/
│       ├── core/           # Core trading logic
│       │   ├── trader.py
│       │   └── trading_floor.py
│       ├── agents/         # AI agents and templates
│       │   └── templates.py
│       ├── market/         # Market data and operations
│       │   ├── market_data.py
│       │   └── server.py
│       ├── accounts/       # Account management
│       │   ├── account.py
│       │   ├── client.py
│       │   └── server.py
│       ├── web/            # Web interface
│       │   ├── app.py
│       │   └── push_server.py
│       ├── utils/          # Utilities and helpers
│       │   ├── database.py
│       │   ├── helpers.py
│       │   ├── tracers.py
│       │   └── reset.py
│       └── config/         # Configuration
│           └── mcp_params.py
├── tests/                  # Test suite
│   ├── unit/
│   └── integration/
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── uv.toml                 # Dependency management
├── setup.py                # Package installation
└── README.md
```

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- `uv` package manager (recommended) or `pip`

### Using uv (Recommended)

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-stock-market-trader.git
   cd ai-stock-market-trader
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

### Using pip

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-stock-market-trader.git
   cd ai-stock-market-trader
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install the package**:
   ```bash
   pip install -e .
   ```

## ⚙️ Configuration

1. **Environment Variables**: Create a `.env` file in the root directory:
   ```bash
   # OpenAI API Keys
   OPENAI_API_KEY=your_openai_api_key
   DEEPSEEK_API_KEY=your_deepseek_api_key
   GOOGLE_API_KEY=your_google_api_key
   GROK_API_KEY=your_grok_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   
   # Polygon API (for market data)
   POLYGON_API_KEY=your_polygon_api_key
   ```

2. **Database**: The system uses SQLite by default. Database files will be created automatically.

## 🚀 Usage

### Web Interface

Run the Gradio web interface:
```bash
# Using the package
python -m ai_stock_trader --mode web

# Or directly
python src/ai_stock_trader/web/app.py
```

### Trading Floor

Run the automated trading system:
```bash
# Using the package
python -m ai_stock_trader --mode trading

# Or directly
python src/ai_stock_trader/core/trading_floor.py
```

### Command Line Interface

The package provides a CLI for various operations:
```bash
ai-stock-trader --mode web      # Run web interface
ai-stock-trader --mode trading  # Run trading floor
```

## 🧪 Testing

Run the test suite:
```bash
# Using uv
uv run pytest

# Using pip
pytest
```

Run with coverage:
```bash
uv run pytest --cov=src --cov-report=html
```

## 🔧 Development

### Code Quality

The project uses several tools for code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

Format and check code:
```bash
# Format code
uv run black src/ tests/
uv run isort src/ tests/

# Lint code
uv run flake8 src/ tests/

# Type check
uv run mypy src/
```

### Pre-commit Hooks

Install pre-commit hooks:
```bash
uv run pre-commit install
```

## 📊 Features in Detail

### AI Trading Agents

- **Researcher Agent**: Analyzes market conditions and company fundamentals
- **Trader Agent**: Makes trading decisions based on research and strategy
- **Multi-Model Support**: Can use different AI models for different tasks

### Market Data

- **Real-time Quotes**: Live stock prices via Polygon API
- **Historical Data**: Access to historical price data
- **Market Status**: Real-time market open/close information

### Portfolio Management

- **Account Tracking**: Monitor multiple trading accounts
- **Holdings**: Track current stock positions
- **Transaction History**: Complete record of all trades
- **Performance Metrics**: Portfolio value and P&L tracking

### Risk Management

- **Position Sizing**: Configurable position limits
- **Stop Losses**: Automated risk controls
- **Diversification**: Strategy-based portfolio allocation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is for educational and research purposes only. It is not intended to provide financial advice or to be used for actual trading without proper risk management and compliance with applicable regulations. Trading stocks involves substantial risk of loss and is not suitable for all investors.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-stock-market-trader/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-stock-market-trader/discussions)
- **Documentation**: Check the `docs/` folder for detailed documentation

## 🙏 Acknowledgments

- OpenAI for the Agents SDK
- Polygon for market data APIs
- The open-source community for various tools and libraries
