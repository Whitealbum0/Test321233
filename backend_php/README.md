# PHP Backend

Простая реализация серверной части на PHP для демонстрации API интернет-магазина.

## Запуск

```bash
php -S localhost:8001 backend_php/server.php
```

Доступные эндпоинты:
- `GET /api/products` – список товаров
- `GET /api/products/{id}` – товар по ID
- `POST /api/products` – создание товара (требуется заголовок `Authorization: Bearer admin`)
- `GET /api/categories` – список категорий
- `GET /health` – проверка состояния сервера
