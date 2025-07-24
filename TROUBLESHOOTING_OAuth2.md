# 🛠️ Устранение неполадок OAuth2

## Часто встречающиеся проблемы и их решения

### 🔐 **Проблемы с авторизацией**

#### 1. **"Invalid client" или "unauthorized_client"**
```
❌ Проблема: Google возвращает ошибку "Invalid client"
```
**Решение:**
- Проверьте `GOOGLE_CLIENT_ID` в `backend/.env`
- Убедитесь, что Client ID правильно скопирован из Google Cloud Console
- Проверьте, что проект в Google Cloud Console активен

#### 2. **"Redirect URI mismatch"**
```
❌ Проблема: Google возвращает ошибку redirect URI
```
**Решение:**
- В Google Cloud Console добавьте: `http://localhost:8001/api/auth/google/callback`
- Убедитесь, что `GOOGLE_REDIRECT_URI` в `.env` совпадает с настройками Google
- Проверьте отсутствие лишних символов или пробелов

#### 3. **"JWT decode error"**
```
❌ Проблема: Ошибка декодирования JWT токена
```
**Решение:**
- Проверьте `JWT_SECRET_KEY` в `.env`
- Убедитесь, что ключ не содержит специальных символов
- Перезапустите backend после изменения ключа

### 🗄️ **Проблемы с базой данных**

#### 1. **MongoDB connection failed**
```
❌ Проблема: Не удается подключиться к MongoDB
```
**Решение:**
```bash
# Проверьте, запущен ли MongoDB
mongo --eval "db.adminCommand('ping')"

# Если MongoDB не установлен, установите:
# Windows: https://www.mongodb.com/try/download/community
# macOS: brew install mongodb-community
# Linux: sudo apt install mongodb

# Запустите MongoDB
mongod
```

#### 2. **Database not found**
```
❌ Проблема: База данных не найдена
```
**Решение:**
```bash
# Запустите скрипт настройки
python setup_oauth2.py

# Или создайте базу вручную
mongo
use ecommerce_local
db.products.insertOne({test: "data"})
```

### 🌐 **Проблемы с сервером**

#### 1. **Port already in use**
```
❌ Проблема: Порт 8001 уже используется
```
**Решение:**
```bash
# Найдите процесс на порту 8001
netstat -ano | findstr :8001

# Завершите процесс
taskkill /PID [PID_NUMBER] /F

# Или используйте другой порт
uvicorn server_oauth:app --port 8002
```

#### 2. **CORS errors**
```
❌ Проблема: CORS ошибки в браузере
```
**Решение:**
- Убедитесь, что frontend запущен на `http://localhost:3000`
- Проверьте настройки CORS в `server_oauth.py`
- Убедитесь, что `FRONTEND_URL` правильно настроен в `.env`

### 🎨 **Проблемы с Frontend**

#### 1. **Module not found: react-query**
```
❌ Проблема: Не найден модуль react-query
```
**Решение:**
```bash
cd frontend
npm install react-query
# или
yarn add react-query
```

#### 2. **OAuth2AuthContext not found**
```
❌ Проблема: Контекст OAuth2 не найден
```
**Решение:**
- Убедитесь, что файл `OAuth2AuthContext.js` существует
- Проверьте импорты в `App_OAuth2.js`
- Убедитесь, что используется правильная версия App.js

### 📱 **Проблемы с Google OAuth2**

#### 1. **Google API not enabled**
```
❌ Проблема: Google+ API не включен
```
**Решение:**
1. Перейдите в Google Cloud Console
2. APIs & Services → Library
3. Найдите "Google+ API"
4. Нажмите "Enable"

#### 2. **Quota exceeded**
```
❌ Проблема: Превышена квота запросов
```
**Решение:**
- Проверьте квоты в Google Cloud Console
- Подождите или увеличьте лимиты
- Используйте другой проект Google Cloud

### 🔧 **Проблемы с конфигурацией**

#### 1. **Environment variables not loaded**
```
❌ Проблема: Переменные окружения не загружаются
```
**Решение:**
```bash
# Проверьте файл .env
cat backend/.env

# Убедитесь, что нет лишних пробелов
# Правильно: GOOGLE_CLIENT_ID=your-id
# Неправильно: GOOGLE_CLIENT_ID = your-id
```

#### 2. **App_OAuth2.js not used**
```
❌ Проблема: Используется старая версия App.js
```
**Решение:**
```bash
cd frontend/src
copy App_OAuth2.js App.js
# или
cp App_OAuth2.js App.js
```

## 🧪 **Диагностические команды**

### Проверка системы
```bash
# Тест OAuth2 системы
python test_oauth2_system.py

# Проверка сервера
curl http://localhost:8001/health

# Проверка OAuth2 redirect
curl -v http://localhost:8001/api/auth/google
```

### Проверка базы данных
```bash
# Подключение к MongoDB
mongo

# Проверка коллекций
use ecommerce_local
db.products.count()
db.users.count()

# Проверка индексов
db.products.getIndexes()
```

### Проверка логов
```bash
# Backend логи
python server_oauth.py

# Frontend логи
npm start

# MongoDB логи
tail -f /var/log/mongodb/mongod.log
```

## 📞 **Получение помощи**

### Пошаговая диагностика
1. **Запустите тест системы**: `python test_oauth2_system.py`
2. **Проверьте логи** backend и frontend
3. **Проверьте переменные окружения**
4. **Убедитесь, что MongoDB запущен**
5. **Проверьте настройки Google OAuth2**

### Полезные ссылки
- [Google Cloud Console](https://console.cloud.google.com/)
- [MongoDB Installation](https://docs.mongodb.com/manual/installation/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Query Documentation](https://react-query.tanstack.com/)

### Создание issue
Если проблема не решена, создайте issue с:
- Описанием проблемы
- Сообщениями об ошибках
- Версиями используемых технологий
- Результатами теста системы

## ✅ **Контрольный список**

Перед использованием убедитесь:
- [ ] MongoDB запущен
- [ ] Переменные окружения настроены
- [ ] Google OAuth2 настроен
- [ ] Все зависимости установлены
- [ ] Порты 3000 и 8001 свободны
- [ ] Файлы OAuth2 существуют
- [ ] Тест системы пройден

---

**💡 Помните:** Большинство проблем связано с неправильной конфигурацией. Внимательно проверьте все настройки!