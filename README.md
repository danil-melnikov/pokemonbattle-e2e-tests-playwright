# Pokemon Battle E2E Tests (Playwright)

Тестовый проект для UI-тестирования тренажёра «Битва покемонов».

## Стек

- **Python** — язык программирования
- **Playwright** — фреймворк для UI-тестирования
- **Pytest** — фреймворк для запуска тестов
- **Page Object Model** — архитектура тестов
- **Allure Report** — отчётность
- **GitLab CI** — запуск тестов в CI/CD

## Структура проекта

- `pages/` — страницы (Page Object Model)
- `tests/api/` — API-тесты
- `tests/e2e/` — E2E-тесты
- `tests/screenshot/` — скриншот-тесты
- `fixtures/` — фикстуры
- `helpers/` — вспомогательные функции
- `data/` — константы
- `config/` — конфигурация

## Запуск тестов

```bash
# Установка зависимостей
pip install -r requirements.txt
playwright install chromium

# Запуск всех тестов
pytest

# Запуск только UI тестов
pytest -m ui

# Запуск smoke тестов
pytest -m smoke

# Запуск с Allure отчётом
pytest --alluredir=allure-results
allure generate allure-results --single-file --output allure-report