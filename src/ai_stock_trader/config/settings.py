"""
Configuration management for AI Stock Trader.
"""

import os
from pathlib import Path
from typing import Optional
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Keys
    openai_api_key: Optional[str] = Field(None, env="OPENAI_API_KEY")
    deepseek_api_key: Optional[str] = Field(None, env="DEEPSEEK_API_KEY")
    google_api_key: Optional[str] = Field(None, env="GOOGLE_API_KEY")
    grok_api_key: Optional[str] = Field(None, env="GROK_API_KEY")
    openrouter_api_key: Optional[str] = Field(None, env="OPENROUTER_API_KEY")
    polygon_api_key: Optional[str] = Field(None, env="POLYGON_API_KEY")
    
    # Database Configuration
    database_url: str = Field("sqlite:///ai_stock_trader.db", env="DATABASE_URL")
    database_path: str = Field("./data/", env="DATABASE_PATH")
    
    # Logging Configuration
    log_level: str = Field("INFO", env="LOG_LEVEL")
    log_file: str = Field("./logs/app.log", env="LOG_FILE")
    log_format: str = Field(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env="LOG_FORMAT"
    )
    
    # Web Interface Configuration
    gradio_server_name: str = Field("0.0.0.0", env="GRADIO_SERVER_NAME")
    gradio_server_port: int = Field(7860, env="GRADIO_SERVER_PORT")
    gradio_share: bool = Field(False, env="GRADIO_SHARE")
    
    # Trading Configuration
    initial_balance: float = Field(10000.0, env="INITIAL_BALANCE")
    spread: float = Field(0.002, env="SPREAD")
    max_position_size: float = Field(0.1, env="MAX_POSITION_SIZE")
    stop_loss_percentage: float = Field(0.05, env="STOP_LOSS_PERCENTAGE")
    
    # Market Data Configuration
    market_data_cache_ttl: int = Field(300, env="MARKET_DATA_CACHE_TTL")
    realtime_data_enabled: bool = Field(True, env="REALTIME_DATA_ENABLED")
    historical_data_days: int = Field(30, env="HISTORICAL_DATA_DAYS")
    
    # AI Agent Configuration
    max_turns: int = Field(30, env="MAX_TURNS")
    research_timeout: int = Field(60, env="RESEARCH_TIMEOUT")
    trading_timeout: int = Field(30, env="TRADING_TIMEOUT")
    
    # MCP Server Configuration
    mcp_server_host: str = Field("localhost", env="MCP_SERVER_HOST")
    mcp_server_port: int = Field(8000, env="MCP_SERVER_PORT")
    
    # Development Configuration
    debug: bool = Field(False, env="DEBUG")
    environment: str = Field("development", env="ENVIRONMENT")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Ensure required directories exist."""
        Path(self.database_path).mkdir(parents=True, exist_ok=True)
        Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.environment.lower() == "production"
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.environment.lower() == "development"
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for a specific provider."""
        api_keys = {
            "openai": self.openai_api_key,
            "deepseek": self.deepseek_api_key,
            "google": self.google_api_key,
            "grok": self.grok_api_key,
            "openrouter": self.openrouter_api_key,
            "polygon": self.polygon_api_key,
        }
        return api_keys.get(provider.lower())


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings
