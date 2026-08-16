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

    # Webhook settings (optional)
    USE_WEBHOOK: bool = Field(default=False, description="Запускати бот через webhook замість polling")
    WEBHOOK_URL: Optional[str] = Field(
        None, description="Публічна URL-адреса для webhook (наприклад https://example.com/webhook)")
    WEBHOOK_HOST: str = Field(default="0.0.0.0", description="Хост для про��луховування webhook")
    WEBHOOK_PORT: int = Field(default=8443, description="Порт для прослуховування webhook")
    WEBHOOK_PATH: str = Field(default="/webhook", description="Local path for webhook endpoint")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
