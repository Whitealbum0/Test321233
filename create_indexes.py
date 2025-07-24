#!/usr/bin/env python3
"""
Скрипт для создания индексов в MongoDB для оптимизации производительности (локальная версия)
"""
import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def create_indexes():
    """Создает индексы для оптимизации запросов"""
    
    # Локальное подключение к MongoDB
    mongo_url = "mongodb://localhost:27017"
    db_name = "ecommerce_local"
    
    print(f"🔌 Подключение к MongoDB: {mongo_url}")
    print(f"📊 База данных: {db_name}")
    
    try:
        client = AsyncIOMotorClient(mongo_url)
        db = client[db_name]
        
        # Проверим подключение
        await client.admin.command('ping')
        print("✅ Подключение к MongoDB успешно!")
        
        print("\n🔧 Создание индексов для оптимизации...")
        
        # Индексы для коллекции products
        await db.products.create_index([("status", 1)])
        print("✅ Индекс по status создан")
        
        await db.products.create_index([("category", 1)])
        print("✅ Индекс по category создан")
        
        await db.products.create_index([("price", 1)])
        print("✅ Индекс по price создан")
        
        await db.products.create_index([("created_at", -1)])
        print("✅ Индекс по created_at создан")
        
        # Составные индексы для более сложных запросов
        await db.products.create_index([("status", 1), ("category", 1)])
        print("✅ Составной индекс по status и category создан")
        
        await db.products.create_index([("status", 1), ("price", 1)])
        print("✅ Составной индекс по status и price создан")
        
        await db.products.create_index([("category", 1), ("price", 1)])
        print("✅ Составной индекс по category и price создан")
        
        # Текстовый индекс для поиска
        try:
            await db.products.create_index([
                ("name", "text"),
                ("description", "text"),
                ("category", "text")
            ])
            print("✅ Текстовый индекс для поиска создан")
        except Exception as e:
            print(f"⚠️ Текстовый индекс уже существует или ошибка: {e}")
        
        # Индексы для коллекции users
        try:
            await db.users.create_index([("email", 1)], unique=True)
            print("✅ Уникальный индекс по email создан")
        except Exception as e:
            print(f"⚠️ Индекс по email уже существует: {e}")
        
        await db.users.create_index([("role", 1)])
        print("✅ Индекс по role создан")
        
        # Индексы для коллекции visitor_logs
        await db.visitor_logs.create_index([("timestamp", -1)])
        print("✅ Индекс по timestamp создан")
        
        await db.visitor_logs.create_index([("user_id", 1)])
        print("✅ Индекс по user_id создан")
        
        await db.visitor_logs.create_index([("page", 1)])
        print("✅ Индекс по page создан")
        
        await db.visitor_logs.create_index([("ip_address", 1)])
        print("✅ Индекс по ip_address создан")
        
        print("\n🎉 Все индексы успешно созданы!")
        print("📊 Теперь запросы к базе данных будут выполняться быстрее")
        
        # Проверим созданные индексы
        print("\n📋 Список индексов для коллекции products:")
        indexes = await db.products.list_indexes().to_list(length=None)
        for idx in indexes:
            print(f"  - {idx['name']}")
            
        # Проверим количество документов
        products_count = await db.products.count_documents({})
        print(f"\n📦 Количество товаров в базе: {products_count}")
        
        if products_count == 0:
            print("⚠️ База данных пуста. Запустите скрипты для добавления товаров:")
            print("   python add_demo_products.py")
            print("   python add_more_products.py")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("💡 Убедитесь, что MongoDB запущен на localhost:27017")
        return False
    finally:
        client.close()
        print("\n✅ Подключение к MongoDB закрыто")
    
    return True

if __name__ == "__main__":
    print("🚀 Оптимизация базы данных MongoDB")
    print("=" * 50)
    
    success = asyncio.run(create_indexes())
    
    if success:
        print("\n🎯 Оптимизация завершена успешно!")
    else:
        print("\n❌ Оптимизация не удалась")