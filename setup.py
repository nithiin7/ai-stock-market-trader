#!/usr/bin/env python3
"""
Setup script for AI Stock Trader package.
"""

from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from uv.toml
def get_requirements():
    """Extract requirements from uv.toml."""
    import re
    with open("uv.toml", "r") as f:
        content = f.read()
    
    # Extract dependencies section
    deps_match = re.search(r'\[project\]\s+dependencies\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if deps_match:
        deps_text = deps_match.group(1)
        # Parse dependencies (simple regex-based parsing)
        deps = []
        for line in deps_text.split('\n'):
            line = line.strip().strip('"').strip("'").strip(',')
            if line and not line.startswith('#') and not line.startswith('['):
                deps.append(line)
        return deps
    return []

setup(
    name="ai-stock-trader",
    version="0.1.0",
    author="AI Stock Trader Team",
    author_email="team@aistocktrader.com",
    description="AI-powered stock market trading system using OpenAI Agents SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-stock-market-trader",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=get_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-stock-trader=ai_stock_trader.__main__:main_cli",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
