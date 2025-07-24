# 🔐 E-commerce с OAuth2 авторизацией

Полнофункциональный интернет-магазин с OAuth2 авторизацией через Google, корзиной покупок и административной панелью.

## ✨ Особенности

### 🔐 **OAuth2 авторизация**
- Вход через Google аккаунт
- Автоматическое создание пользователей
- JWT токены для безопасности
- Связывание аккаунтов

### 🛒 **Функциональность магазина**
- Каталог товаров с фильтрацией
- Корзина покупок
- Система категорий
- Адаптивный дизайн

### ⚡ **Высокая производительность**
- React Query для кеширования
- Lazy loading компонентов
- Виртуализация списков
- Service Worker для offline

### 📱 **Мультиплатформенность**
- Отдельные интерфейсы для Desktop и Mobile
- Автоматическое определение устройства
- Переключение между режимами

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
# Запустите setup скрипт
setup_oauth2_all.bat

# Или вручную:
pip install -r backend/requirements_oauth2.txt
cd frontend && npm install
```

### 2. Настройка Google OAuth2

1. **Перейдите в Google Cloud Console**: https://console.cloud.google.com/
2. **Создайте проект** или выберите существующий
3. **Включите Google+ API**
4. **Создайте OAuth2 Client ID**:
   - Тип: Web application
   - Authorized redirect URI: `http://localhost:8001/api/auth/google/callback`
5. **Скопируйте Client ID и Client Secret**

### 3. Настройка переменных окружения

Обновите `backend/.env`:
```env
GOOGLE_CLIENT_ID=ваш-google-client-id
GOOGLE_CLIENT_SECRET=ваш-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8001/api/auth/google/callback
JWT_SECRET_KEY=ваш-супер-секретный-ключ
MONGO_URL=mongodb://localhost:27017
DB_NAME=ecommerce_local
FRONTEND_URL=http://localhost:3000
```

### 4. Запуск приложения

```bash
# Backend (в первом терминале)
start_oauth2_backend.bat

# Frontend (во втором терминале)
start_oauth2_frontend.bat
```

## 📊 Технологии

### Backend
- **FastAPI** - Современный Python веб-фреймворк
- **MongoDB** - NoSQL база данных
- **JWT** - Токены для авторизации
- **OAuth2** - Стандарт авторизации
- **Motor** - Асинхронный драйвер MongoDB

### Frontend
- **React 19** - Пользовательский интерфейс
- **React Query** - Кеширование данных
- **Tailwind CSS** - Стилизация
- **React Router** - Роутинг
- **Axios** - HTTP клиент

## 🔧 Архитектура

```
ecommerce-oauth2/
├── backend/
│   ├── oauth_auth.py           # OAuth2 логика
│   ├── server_oauth.py         # FastAPI сервер
│   ├── requirements_oauth2.txt # Зависимости
│   └── .env                    # Переменные окружения
├── frontend/
│   ├── src/
│   │   ├── contexts/
│   │   │   ├── OAuth2AuthContext.js    # OAuth2 контекст
│   │   │   ├── CartContext.js          # Корзина
│   │   │   └── DeviceContext.js        # Устройство
│   │   ├── components/
│   │   │   ├── Auth/
│   │   │   │   └── GoogleLoginButton.js
│   │   │   ├── Desktop/
│   │   │   │   └── DesktopNavbarOAuth2.js
│   │   │   ├── Mobile/
│   │   │   │   └── MobileNavbarOAuth2.js
│   │   │   └── Common/
│   │   └── App_OAuth2.js       # Главное приложение
│   ├── package.json
│   └── .env
└── setup_oauth2.py             # Скрипт настройки
```

## 🔐 Безопасность

### JWT токены
- Время жизни: 30 минут
- Алгоритм: HS256
- Автоматическое обновление

### Защищенные маршруты
- Публичные: товары, категории
- Приватные: профиль, корзина
- Админские: управление пользователями

### OAuth2 Flow
1. Пользователь нажимает "Войти через Google"
2. Перенаправление на Google OAuth2
3. Пользователь авторизуется в Google
4. Google возвращает код авторизации
5. Backend обменивает код на токен
6. Получение информации о пользователе
7. Создание/обновление пользователя в БД
8. Создание JWT токена
9. Перенаправление на frontend с токеном

## 📱 API Endpoints

### Авторизация
- `GET /api/auth/google` - Вход через Google
- `GET /api/auth/google/callback` - Callback от Google  
- `POST /api/auth/google/mobile` - Мобильная авторизация
- `GET /api/auth/me` - Информация о пользователе
- `POST /api/auth/logout` - Выход

### Товары
- `GET /api/products` - Список товаров
- `GET /api/categories` - Категории
- `GET /api/categories/stats` - Статистика категорий

### Администрирование
- `GET /api/admin/users` - Пользователи
- `GET /api/admin/stats` - Статистика

## 🎯 Роли пользователей

### User (Пользователь)
- Просмотр товаров
- Добавление в корзину
- Оформление заказов
- Управление профилем

### Admin (Администратор)
- Все права пользователя
- Управление товарами
- Управление пользователями
- Просмотр аналитики

## 🔧 Настройка для Production

### 1. Переменные окружения
```env
# Production настройки
JWT_SECRET_KEY=very-long-random-secret-key
GOOGLE_REDIRECT_URI=https://yourdomain.com/api/auth/google/callback
FRONTEND_URL=https://yourdomain.com
MONGO_URL=mongodb://your-production-db
```

### 2. Google OAuth2
- Добавьте production домен в Authorized redirect URIs
- Используйте разные Client ID для development и production

### 3. Безопасность
- Используйте HTTPS
- Настройте CORS правильно
- Используйте strong JWT secret
- Включите rate limiting

## 🐛 Отладка

### Проверка настроек
```bash
# Проверка Google OAuth2
curl http://localhost:8001/api/auth/google

# Проверка подключения к MongoDB
mongo --eval "db.adminCommand('ping')"

# Проверка JWT токена
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8001/api/auth/me
```

### Логи
- Backend: Консоль uvicorn
- Frontend: Developer Tools
- MongoDB: Database logs

## 🆘 Поддержка

### Частые проблемы
1. **Google OAuth2 не работает** - Проверьте Client ID/Secret
2. **Redirect URI mismatch** - Проверьте настройки в Google Console
3. **JWT токен недействителен** - Проверьте secret key
4. **MongoDB connection failed** - Убедитесь что MongoDB запущен

### Помощь
- Изучите `OAuth2_SETUP_GUIDE.md`
- Проверьте логи в консоли
- Убедитесь что все зависимости установлены

## 📄 Лицензия

MIT License - см. файл LICENSE

## 👥 Авторы

Создано с использованием современных технологий веб-разработки.

---

**🎉 Готово к использованию!** Следуйте инструкциям выше для быстрого старта.