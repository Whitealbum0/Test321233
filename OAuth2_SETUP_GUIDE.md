# 🔐 Настройка OAuth2 с Google авторизацией

## 📋 Руководство по настройке OAuth2 для e-commerce приложения

### 🎯 **Что было реализовано:**

1. **OAuth2 авторизация с Google**
2. **JWT токены для сессий**
3. **Автоматическое создание пользователей**
4. **Связывание аккаунтов**
5. **Защищенные маршруты**

---

## 🚀 **Быстрый старт:**

### **1. Установка зависимостей:**

```bash
# Backend
cd backend
pip install -r requirements_oauth2.txt

# Frontend
cd frontend
npm install
```

### **2. Настройка базы данных:**

```bash
# Запустите скрипт настройки OAuth2
python setup_oauth2.py
```

### **3. Настройка Google OAuth2:**

#### **A. Создание проекта в Google Cloud Console:**

1. **Перейдите в Google Cloud Console**: https://console.cloud.google.com/
2. **Создайте новый проект** или выберите существующий
3. **Включите Google+ API**:
   - Перейдите в "APIs & Services" → "Library"
   - Найдите "Google+ API"
   - Нажмите "Enable"

#### **B. Создание OAuth2 Client ID:**

1. **Перейдите в "Credentials"**: APIs & Services → Credentials
2. **Нажмите "Create Credentials"** → "OAuth 2.0 Client ID"
3. **Выберите тип**: "Web application"
4. **Настройте redirect URI**:
   ```
   Authorized redirect URIs:
   http://localhost:8001/api/auth/google/callback
   ```
5. **Скачайте credentials** или скопируйте Client ID и Client Secret

#### **C. Настройка переменных окружения:**

Обновите `backend/.env`:
```env
# OAuth2 Configuration
GOOGLE_CLIENT_ID=ваш-google-client-id
GOOGLE_CLIENT_SECRET=ваш-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8001/api/auth/google/callback

# JWT Configuration
JWT_SECRET_KEY=ваш-супер-секретный-ключ

# Database Configuration
MONGO_URL=mongodb://localhost:27017
DB_NAME=ecommerce_local

# Frontend URL
FRONTEND_URL=http://localhost:3000
```

### **4. Запуск приложения:**

```bash
# Backend (в первом терминале)
cd backend
python server_oauth.py

# Frontend (во втором терминале)
cd frontend
npm start
```

### **5. Тестирование:**

- Откройте http://localhost:3000
- Нажмите "Войти"
- Выберите "Войти через Google"
- Авторизуйтесь с помощью Google аккаунта

---

## 🔧 **Структура OAuth2 системы:**

### **Backend файлы:**
- `oauth_auth.py` - Основная логика OAuth2
- `server_oauth.py` - FastAPI сервер с OAuth2
- `requirements_oauth2.txt` - Зависимости

### **Frontend файлы:**
- `OAuth2AuthContext.js` - Context для авторизации
- `GoogleLoginButton.js` - Компонент входа
- `DesktopNavbarOAuth2.js` - Десктопная навигация
- `MobileNavbarOAuth2.js` - Мобильная навигация

### **Основные endpoints:**
- `GET /api/auth/google` - Перенаправление на Google
- `GET /api/auth/google/callback` - Callback от Google
- `POST /api/auth/google/mobile` - Мобильная авторизация
- `GET /api/auth/me` - Информация о пользователе
- `POST /api/auth/logout` - Выход из системы

---

## 🛡️ **Безопасность:**

### **JWT токены:**
- Время жизни: 30 минут
- Алгоритм: HS256
- Автоматическое обновление

### **Защищенные маршруты:**
- `get_current_user()` - Обязательная авторизация
- `get_current_user_optional()` - Опциональная авторизация
- `get_admin_user()` - Только для админов

### **Данные пользователя:**
- Email (обязательно)
- Имя (из Google)
- Фото профиля (из Google)
- Роль (user/admin)
- Дата создания

---

## 📊 **Административные функции:**

### **Роли пользователей:**
- **user** - Обычный пользователь
- **admin** - Администратор

### **Админские endpoints:**
- `GET /api/admin/users` - Список пользователей
- `GET /api/admin/stats` - Статистика

### **Создание админа:**
```python
# Вручную через MongoDB
db.users.update_one(
    {"email": "admin@example.com"},
    {"$set": {"role": "admin"}}
)
```

---

## 🔍 **Отладка:**

### **Проверка настроек:**
```bash
# Проверка переменных окружения
cat backend/.env

# Проверка подключения к MongoDB
mongo --eval "db.adminCommand('ping')"

# Проверка Google OAuth2
curl http://localhost:8001/api/auth/google
```

### **Логи:**
- Backend: Консоль uvicorn
- Frontend: Консоль браузера
- MongoDB: Логи MongoDB

### **Типичные ошибки:**
1. **Неверный Client ID** - Проверьте `.env`
2. **Неверный Redirect URI** - Проверьте настройки в Google Console
3. **MongoDB не запущен** - Запустите MongoDB
4. **Порт занят** - Используйте другой порт

---

## 🎉 **Готово!**

Теперь у вас есть полнофункциональная OAuth2 авторизация:

✅ **Вход через Google**
✅ **Автоматическое создание пользователей**
✅ **JWT токены**
✅ **Защищенные маршруты**
✅ **Административные функции**
✅ **Мобильная поддержка**

### **Следующие шаги:**
1. Настройте production переменные окружения
2. Добавьте SSL сертификаты
3. Настройте backup базы данных
4. Добавьте мониторинг

**Удачи в использовании OAuth2 авторизации! 🚀**