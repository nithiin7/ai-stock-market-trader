.PHONY: help install install-dev test test-cov format lint type-check clean run-web run-trading build publish

help: ## Show this help message
	@echo "AI Stock Trader - Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	uv sync

install-dev: ## Install the package with development dependencies
	uv sync --extra dev

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=src --cov-report=html --cov-report=term-missing

format: ## Format code with black and isort
	uv run black src/ tests/
	uv run isort src/ tests/

lint: ## Lint code with flake8
	uv run flake8 src/ tests/

type-check: ## Type check with mypy
	uv run mypy src/

check: format lint type-check ## Run all code quality checks

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run-web: ## Run the web interface
	uv run python -m ai_stock_trader --mode web

run-trading: ## Run the trading floor
	uv run python -m ai_stock_trader --mode trading

build: ## Build the package
	uv run python -m build

publish: ## Publish to PyPI (requires authentication)
	uv run python -m twine upload dist/*

dev-setup: install-dev ## Set up development environment
	uv run pre-commit install

docker-build: ## Build Docker image
	docker build -t ai-stock-trader .

docker-run: ## Run Docker container
	docker run -p 7860:7860 ai-stock-trader

# Database operations
db-reset: ## Reset the database
	uv run python src/ai_stock_trader/utils/reset.py

# Environment setup
env-example: ## Create example environment file
	cp .env.example .env

# Documentation
docs-serve: ## Serve documentation locally
	uv run mkdocs serve

docs-build: ## Build documentation
	uv run mkdocs build

# Monitoring and debugging
logs: ## Show application logs
	tail -f logs/app.log

status: ## Show system status
	@echo "Python version:"
	@python --version
	@echo "UV version:"
	@uv --version
	@echo "Installed packages:"
	@uv pip list
