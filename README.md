# Stripe Payment Demo

## Краткое описание

Данный проект представляет собой демонстрационное веб-приложение для тестирования интеграции с платёжной системой Stripe. Приложение позволяет пользователю выбрать товар, ввести тестовые платёжные данные и выполнить оплату. Реализована обработка успешных и неуспешных платежей, а также вебхуки для получения событий от Stripe.

## Скриншот интерфейса

![alt text](images/image.png)

![alt text](images/image-1.png)

![alt text](images/image-2.png)

## Структура и архитектура проекта

```text
├─── .env_example                   # Пример переменных окружения
├─── .gitignore
├─── docker-compose.yml
├─── README.md
│   
├───backend                           # Бэкенд на FastAPI
│   │   alembic.ini                    # Конфигурация миграций БД
│   │   config.py                       # Настройки приложения
│   │   dependencies.py                  # Общие зависимости
│   │   Dockerfile
│   │   entrypoint.sh                      # Скрипт запуска контейнера
│   │   main.py                             # Точка входа приложения
│   │   requirements.txt                     # Зависимости Python
│   │   
│   ├───alembic                             # Миграции базы данных
│   │   │   
│   │   ├───versions                          # Файлы миграций
│   │           
│   ├───database                             # Работа с БД
│   │   │   base.py                            # Базовый класс моделей
│   │   │   create_mock_products.py             # Генерация тестовых данных
│   │   │   database_connection.py               # Подключение к БД
│   │   │   engine.py                            # Движок SQLAlchemy
│   │   │   products.py                          # Модель продуктов
│   │   │   __init__.py
│   │           
│   ├───di                                   # Dependency Injection
│   │   │   container.py                       # Контейнер зависимостей
│   │   │   __init__.py
│   │           
│   ├───dto                                  # Data Transfer Objects
│   │       products_dto.py                     # Схемы продуктов
│   │       __init__.py
│   │       
│   ├───repositories                         # Слой доступа к данным
│   │   │   product_repository.py               # CRUD операции с продуктами
│   │   │   __init__.py
│   │           
│   ├───routers                              # Маршруты API
│   │   │   payments.py                         # Эндпоинты платежей
│   │   │   products.py                          # Эндпоинты продуктов
│   │   │   __init__.py
│   │   │   
│   │           
│   ├───services                             # Бизнес-логика
│   │   │   payment_service.py                   # Логика платежей
│   │   │   product_service.py                    # Логика продуктов
│   │   │   __init__.py  
│                   
├───frontend                                # Фронтенд на React/TypeScript
│   │   .gitignore
│   │   Dockerfile
│   │   package-lock.json
│   │   package.json
│   │   README.md
│   │   tsconfig.json
│   └───src                                      # Исходный код
│       │   .env_example                             # Пример переменных окружения
│       │   App.css
│       │   App.tsx                                    # Главный компонент
│       │   index.css                                   # Глобальные стили
│       │   index.tsx                                    # Точка входа React
│       │   logo.svg                                      # Логотип
│       │   reportWebVitals.js                            # Метрики производительности
│       │   setupTests.js                                  # Настройки тестов
│       │   
│       ├───api                                        # API клиент
│       │       api.tsx                                   # Запросы к бэкенду
│       │       
│       ├───components                                 # React компоненты
│       │       ProductsComponent.tsx                      # Отображение продуктов
│       │       styles.css                                   # Стили компонентов
│       │       SuccessComponent.tsx                         # Страница успеха
│       │       
│       └───interfaces                                  # TypeScript интерфейсы
│               ProductInterface.tsx                        # Типы продуктов
│               
├───images                                       # Изображения для документации
│       image-1.png
│       image-2.png
│       image.png
```

## Шаги по запуску

1. Клонировать репозиторий:

```bash
git clone https://github.com/vitos63/stripe-payment.git
cd stripe-payment
```
2. Настроить переменные окружения:

Скопировать файл .env_example в .env:

```bash
cp .env_example .env
```

3. Поднять docker контейнеры командой

``` bash
docker compose up --build -d
```

4. Открыть приложение в браузере по пути http://localhost:3000/

``` bash
docker compose up --build -d
```

## Описание переменных окружения

``` .env
DATABASE_URL=postgresql+asyncpg://user:pass@host/db_name
DATABASE_HOST=host
DATABASE_PORT=5432
DATABASE_NAME=db_name
DATABASE_USER=user
DATABASE_PASSWORD=pass
FRONTEND_URL=http://localhost:3000      # Путь по которому разворачивается frontend приложения
STRIPE_SECRET_KEY=sk_test_...           # Приватный ключ Stripe, который необходимо получить в личном кабинете Stripe
STRIPE_WEBHOOK=whsec_...                # Вебхук Stripe, необходимый для отслеживания событий
```

## Как протестировать оплату?

Для каждого сценария, необходимо ввести следующий номер карты.
Используйте любую будущую дату истечения срока действия (например, 12/34) и любой 3-значный CVC-код.

|         Сценарий            |      Номер карты      |
|-----------------------------|-----------------------|
| Успех                       | 4242 4242 4242 4242   |
| Отказ                       | 4000 0000 0000 0002   |
| Требуется аутентификация    | 4000 0025 0000 3155   |


## Интеграция веб-хуков

Когда в Stripe происходят определенные события (платеж успешно завершен, подписка отменена и т. д.), 
Stripe отправляет HTTP POST-запрос на ваш сервер с подробной информацией о событии.

Для того, чтобы протестировать веб-хуки необходимо установить Stripe-CLI

``` bash
# Login
stripe login

# Forward webhooks to localhost
stripe listen --forward-to localhost:8000/webhook
```

Это даст вам секретный ключ для подписи вебхука. Добавьте его в свой файл .env:

``` .env
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxx
```

Запуск тестовых событий:

``` bash
stripe trigger checkout.session.completed
stripe trigger customer.subscription.deleted
stripe trigger invoice.payment_failed
```
