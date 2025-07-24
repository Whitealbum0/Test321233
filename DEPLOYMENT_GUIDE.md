# Руководство по локальному развертыванию

## Обзор приложения

Интернет-магазин с полнофункциональными возможностями:
- **Frontend**: React 18 с Tailwind CSS
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Authentication**: Emergent Authentication
- **Features**: Каталог товаров, категории, фильтрация, поиск, адаптивный дизайн

## Предварительные требования

### Windows 10/11
1. **Node.js** (версия 16 или выше)
   - Скачать: https://nodejs.org/
   - Проверить: `node --version` и `npm --version`

2. **Python** (версия 3.8 или выше)
   - Скачать: https://python.org/downloads/
   - Проверить: `python --version` и `pip --version`

3. **MongoDB Community Edition**
   - Скачать: https://www.mongodb.com/try/download/community
   - Или использовать MongoDB Atlas (облачная база данных)

4. **Git**
   - Скачать: https://git-scm.com/download/win

## Пошаговая установка

### 1. Клонирование проекта
```bash
git clone [URL_ВАШЕГО_РЕПОЗИТОРИЯ]
cd [ИМЯ_ПРОЕКТА]
```

### 2. Настройка Backend
```bash
cd backend
pip install -r requirements.txt
```
cd backend
pip install -r requirements.txt
cd -
### 3. Настройка Frontend
```bash
cd frontend
npm install
```

### 4. Конфигурация базы данных

#### Вариант A: Локальная MongoDB
1. Установить MongoDB Community Edition
2. Запустить MongoDB службу
3. Создать файл `backend/.env`:
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=ecommerce_local
```

#### Вариант B: MongoDB Atlas (рекомендуется)
1. Создать бесплатный аккаунт на https://mongodb.com/atlas
2. Создать кластер
3. Получить строку подключения
4. Создать файл `backend/.env`:
```env
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=ecommerce_local
```

### 5. Конфигурация Frontend
Создать файл `frontend/.env`:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

### 6. Наполнение базы данных (опционально)
```bash
cd backend
python ../add_demo_products.py
python ../add_more_products.py
```

## Запуск приложения

### 1. Запуск Backend
```bash
cd backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### 2. Запуск Frontend (в новом терминале)
```bash
cd frontend
npm start
```

### 3. Доступ к приложению
- Frontend: http://localhost:3000
- Backend API: http://localhost:8001/api

## Структура проекта

```
ecommerce-app/
├── backend/                 # FastAPI приложение
│   ├── server.py           # Основной файл API
│   ├── requirements.txt    # Python зависимости
│   └── .env               # Переменные окружения
├── frontend/               # React приложение
│   ├── src/
│   │   ├── components/    # Компоненты UI
│   │   │   ├── Desktop/   # Десктопные компоненты
│   │   │   ├── Mobile/    # Мобильные компоненты
│   │   │   └── Common/    # Общие компоненты
│   │   ├── contexts/      # React контексты
│   │   ├── hooks/         # Пользовательские хуки
│   │   └── utils/         # Утилиты
│   ├── package.json       # Node.js зависимости
│   └── .env              # Переменные окружения
├── add_demo_products.py   # Скрипт для наполнения данными
├── add_more_products.py   # Дополнительные товары
└── README.md             # Документация
```

## Функциональность

### Основные возможности
- ✅ Адаптивный дизайн (Desktop/Mobile)
- ✅ Каталог товаров с фильтрацией
- ✅ Поиск по товарам
- ✅ Категории товаров
- ✅ Сортировка по цене, названию, дате
- ✅ Аутентификация пользователей
- ✅ Ролевая система (Admin/User)
- ✅ Отслеживание посетителей
- ✅ Аналитика (для админов)

### API Endpoints
- `GET /api/products` - Получить товары
- `GET /api/categories` - Получить категории
- `GET /api/categories/stats` - Статистика категорий
- `POST /api/auth/session` - Аутентификация
- `GET /api/admin/analytics` - Аналитика (admin)

## Решение проблем

### Проблема: MongoDB не запускается
- Проверить службу MongoDB в диспетчере задач
- Перезапустить службу MongoDB
- Проверить логи MongoDB

### Проблема: Backend не может подключиться к DB
- Проверить строку подключения в `.env`
- Убедиться, что MongoDB запущена
- Проверить права доступа к базе данных

### Проблема: Frontend не может подключиться к Backend
- Проверить, что backend запущен на порту 8001
- Проверить переменную `REACT_APP_BACKEND_URL` в frontend/.env
- Проверить CORS настройки

### Проблема: Товары не отображаются
- Запустить скрипты наполнения данными
- Проверить подключение к базе данных
- Проверить консоль браузера на ошибки

## Дополнительные возможности

### Добавление товаров
Создать админский аккаунт и использовать API для добавления товаров:
```python
# Пример создания товара
import requests

data = {
    "name": "Новый товар",
    "description": "Описание товара",
    "price": 1000,
    "category": "Электроника",
    "stock": 10,
    "images": ["base64_image_data"]
}

response = requests.post("http://localhost:8001/api/products", json=data)
```

### Настройка для production
1. Изменить URL в `frontend/.env` на production адрес
2. Настроить SSL сертификаты
3. Настроить reverse proxy (nginx)
4. Настроить переменные окружения для production

## Контакты и поддержка

Если возникают проблемы:
1. Проверить логи backend и frontend
2. Убедиться, что все зависимости установлены
3. Проверить версии Node.js и Python
4. Проверить подключение к MongoDB

Удачи в использовании интернет-магазина! 🛍️