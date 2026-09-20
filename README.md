# Автотесты сервиса аренды самокатов (UI)

Автоматизированные UI-тесты для сервиса аренды самокатов, реализованные с использованием паттерна Page Object.

## Технологии
- Python 3.10+
- Pytest
- Selenium WebDriver
- Allure (отчётность)

## Что покрыто тестами
- Оформление заказа (`test_order.py`)
- Раздел FAQ (`test_faq.py`)
- Навигация по сайту (`test_navigation.py`)

## Структура проекта
```
Sprint_6/
├── pages/            — Page Object классы
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
├── tests/            — тест-кейсы
│   ├── test_faq.py
│   ├── test_order.py
│   └── test_navigation.py
├── conftest.py       — фикстуры
├── data.py           — тестовые данные
├── locators.py       — локаторы элементов
└── requirements.txt
```

## Как запустить
```bash
git clone https://github.com/Ximikkirito/Sprint_6.git
cd Sprint_6
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

Генерация отчёта:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
