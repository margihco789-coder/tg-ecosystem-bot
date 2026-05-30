from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    """
    Конфігурація бота.
    Всі секрети беруться з .env файлу.
    """

    # Telegram
    BOT_TOKEN: str = Field(..., description="Токен твого Telegram бота")

    # Webhook з сайту (опціонально)
    SITE_WEBHOOK_SECRET: Optional[str] = Field(
        None, description="Секрет для webhook з сайту"
    )

    # Твоє API (вставляєш сам)
    YOUR_API_BASE_URL: Optional[str] = Field(
        None, description="Базовий URL твого API"
    )
    YOUR_API_KEY: Optional[str] = Field(
        None, description="Ключ доступу до твого API"
    )

    # Redis (рекомендую для production)
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0",
        description="Redis для FSM та кешу"
    )

    # Режим
    DEBUG: bool = Field(default=True)
    LOG_LEVEL: str = Field(default="INFO")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()