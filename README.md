# TG Ecosystem Bot v160.0

**Частина єдиної екосистеми Markiian Hyshko Engineering Bureau**

> Автономний Telegram-бот, який працює як точка входу, кваліфікації лідів та інтеграції з веб-сайтом і AI-ядром (VEXORA-style).

---

## Місце в екосистемі

Цей бот — **серце комунікації** між:

- Веб-сайтом (`crimson-evangeline-20.tiiny.site` та майбутнім hyshko.io)
- Тобою (особисті повідомлення)
- AI Core (агенти, пам'ять, оркестрація)
- Клієнтами та проєктами

Діаграма всієї екосистеми: дивись файл `Markiian_Ecosystem_Architecture_v160.md`

---

## Що вміє бот (базова версія)

- Приймати ліди з веб-сайту (через webhook)
- Кваліфікувати ліди в чаті
- Зберігати контекст і пам'ять про користувача
- Надсилати нотифікації тобі
- Бути готовим до підключення твого API (ти вставляєш сам)
- Підготовлений до інтеграції з VEXORA / AI-агентами

---

## Структура проєкту (чиста архітектура)

```
tg-ecosystem-bot/
├── bot/
│   ├── handlers/          # Обробники повідомлень
│   ├── middlewares/       # Middleware (auth, logging, rate limit)
│   ├── services/          # Бізнес-логіка
│   └── keyboards/         # Клавіатури
├── core/
│   ├── config.py          # Налаштування (Pydantic)
│   └── di.py              # Dependency Injection
├── integrations/
│   ├── site_webhook.py    # Webhook з сайту
│   └── user_bot_api.py    # ← ТВОЯ API ТОЧКА (вставляєш сам)
├── models/                # Pydantic моделі
├── repositories/          # Робота з БД / Redis
├── docs/
│   └── architecture.md
├── main.py
└── README.md
```

---

## Як запустити (локально)

1. Створи `.env` файл (приклад нижче)
2. `pip install -r requirements.txt`
3. `python main.py`

---

## Твоя точка вставки API

У файлі `integrations/user_bot_api.py` є чітко позначене місце:

```python
# === ТВОЯ API ТОЧКА ВСТАВКИ ===
# curl -fsSL https://x.ai/cli/install.sh | bashСюди вставляй виклики до свого API / сервісів
async def process_lead_with_your_api(lead_data: dict):
    ...
```

Бот повністю готовий до того, щоб ти підключив свій API без зміни основної архітектури.

---

## Наступні кроки (рекомендую по порядку)

1. Встав свій TG Bot API в `integrations/user_bot_api.py`
2. Налаштуй webhook з сайту (`integrations/site_webhook.py`)
3. Додай Redis + SQLAlchemy (якщо потрібно)
4. Підключи до VEXORA / AI Core
5. Деплой на сервер (Docker ready)

---

## Філософія

- Чиста архітектура
- Готовий до агентного майбутнього
- Мінімум залежностей на старті
- Максимум розширюваності
- Рівень коду: той, до якого людство дійде через 160 років

---

**Створено для Markiian Hyshko**  
Engineering Bureau v160.0

Готовий до GitHub. Готовий до зростання.
