#!/usr/bin/env python3
"""
Скрипт для добавления демонстрационных товаров в MongoDB (локальная версия)
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uuid

async def add_demo_products():
    """Добавляет демонстрационные товары в базу данных"""
    
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
        
        # Демонстрационные товары
        demo_products = [
            {
                "id": str(uuid.uuid4()),
                "name": "Беспроводные наушники Pro",
                "description": "Высококачественные беспроводные наушники с активным шумоподавлением",
                "price": 15999.99,
                "category": "Электроника",
                "stock": 10,
                "images": [],
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Смартфон Galaxy Max",
                "description": "Современный смартфон с отличной камерой и быстрым процессором",
                "price": 89999.99,
                "category": "Электроника",
                "stock": 5,
                "images": [],
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Кроссовки для бега",
                "description": "Комфортные кроссовки для бега и спорта",
                "price": 8999.99,
                "category": "Спорт и фитнес",
                "stock": 15,
                "images": [],
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Увлажняющий крем",
                "description": "Питательный крем для всех типов кожи",
                "price": 2799.99,
                "category": "Красота и здоровье",
                "stock": 20,
                "images": [],
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Кофеварка эспрессо",
                "description": "Автоматическая кофеварка для приготовления эспрессо",
                "price": 45999.99,
                "category": "Дом и быт",
                "stock": 3,
                "images": [],
                "status": "active",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        
        # Очистим коллекцию товаров
        await db.products.delete_many({})
        print("🗑️ Старые товары удалены")
        
        # Добавим новые товары
        result = await db.products.insert_many(demo_products)
        print(f"✅ Добавлено {len(result.inserted_ids)} товаров")
        
        # Проверим результат
        count = await db.products.count_documents({})
        print(f"📦 Всего товаров в базе: {count}")
        
        # Покажем категории
        categories = await db.products.distinct("category")
        print(f"📂 Категории: {categories}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
    finally:
        client.close()
        print("✅ Подключение к MongoDB закрыто")
    
    return True

if __name__ == "__main__":
    print("🛒 Добавление демонстрационных товаров")
    print("=" * 50)
    
    success = asyncio.run(add_demo_products())
    
    if success:
        print("\n🎯 Товары добавлены успешно!")
    else:
        print("\n❌ Не удалось добавить товары")