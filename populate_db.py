#!/usr/bin/env python
"""
Script para poblar la base de datos con datos de prueba.

Uso:
    python populate_db.py

Este script creará:
- Varios usuarios de prueba
- Múltiples categorías
- Productos variados en diferentes categorías
"""

import os
import sys
import django
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import Category, Product


def clear_data():
    """Limpiar datos existentes"""
    print("🗑️  Limpiando datos existentes...")
    Product.objects.all().delete()
    Category.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()
    print("✓ Datos limpiados")


def create_users():
    """Crear usuarios de prueba"""
    print("\n👥 Creando usuarios...")
    users = []

    # Usuario administrador (si no existe)
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        users.append(admin)
        print(f"  ✓ Superusuario creado: admin / admin123")

    # Usuarios regulares
    regular_users_data = [
        {'username': 'juan', 'email': 'juan@example.com', 'first_name': 'Juan', 'last_name': 'Pérez'},
        {'username': 'maria', 'email': 'maria@example.com', 'first_name': 'María', 'last_name': 'García'},
        {'username': 'carlos', 'email': 'carlos@example.com', 'first_name': 'Carlos', 'last_name': 'López'},
    ]

    for user_data in regular_users_data:
        user = User.objects.create_user(
            password='password123',
            **user_data
        )
        users.append(user)
        print(f"  ✓ Usuario creado: {user.username} / password123")

    return users


def create_categories():
    """Crear categorías de productos"""
    print("\n📁 Creando categorías...")
    categories_data = [
        {
            'name': 'Electrónica',
            'description': 'Productos electrónicos y tecnología'
        },
        {
            'name': 'Ropa',
            'description': 'Prendas de vestir y accesorios'
        },
        {
            'name': 'Hogar',
            'description': 'Artículos para el hogar y decoración'
        },
        {
            'name': 'Libros',
            'description': 'Libros físicos y digitales'
        },
        {
            'name': 'Deportes',
            'description': 'Artículos deportivos y fitness'
        },
        {
            'name': 'Alimentos',
            'description': 'Alimentos y bebidas'
        },
    ]

    categories = []
    for cat_data in categories_data:
        category = Category.objects.create(**cat_data)
        categories.append(category)
        print(f"  ✓ Categoría creada: {category.name}")

    return categories


def create_products(categories, users):
    """Crear productos de ejemplo"""
    print("\n📦 Creando productos...")

    products_data = [
        # Electrónica
        {
            'name': 'iPhone 15 Pro',
            'description': 'Smartphone Apple con chip A17 Pro, cámara de 48MP y pantalla Super Retina XDR',
            'price': Decimal('999.99'),
            'category': categories[0],
            'stock': 50,
            'is_active': True,
            'created_by': users[1]
        },
        {
            'name': 'MacBook Pro 14"',
            'description': 'Laptop profesional con chip M3 Pro, 16GB RAM, 512GB SSD',
            'price': Decimal('1999.00'),
            'category': categories[0],
            'stock': 25,
            'is_active': True,
            'created_by': users[1]
        },
        {
            'name': 'Samsung Galaxy S24',
            'description': 'Smartphone Android con cámara de 200MP y pantalla AMOLED',
            'price': Decimal('899.99'),
            'category': categories[0],
            'stock': 40,
            'is_active': True,
            'created_by': users[2]
        },
        {
            'name': 'iPad Air',
            'description': 'Tablet con pantalla de 10.9", chip M2 y Apple Pencil compatible',
            'price': Decimal('599.00'),
            'category': categories[0],
            'stock': 30,
            'is_active': True,
            'created_by': users[1]
        },
        {
            'name': 'AirPods Pro',
            'description': 'Auriculares inalámbricos con cancelación activa de ruido',
            'price': Decimal('249.00'),
            'category': categories[0],
            'stock': 5,  # Stock bajo para pruebas
            'is_active': True,
            'created_by': users[2]
        },

        # Ropa
        {
            'name': 'Camiseta Nike Dri-FIT',
            'description': 'Camiseta deportiva transpirable, talla M',
            'price': Decimal('29.99'),
            'category': categories[1],
            'stock': 100,
            'is_active': True,
            'created_by': users[2]
        },
        {
            'name': 'Jeans Levi\'s 501',
            'description': 'Pantalón vaquero clásico, corte recto, talla 32',
            'price': Decimal('79.99'),
            'category': categories[1],
            'stock': 60,
            'is_active': True,
            'created_by': users[3]
        },
        {
            'name': 'Chaqueta North Face',
            'description': 'Chaqueta impermeable para montaña, talla L',
            'price': Decimal('149.99'),
            'category': categories[1],
            'stock': 8,  # Stock bajo
            'is_active': True,
            'created_by': users[2]
        },

        # Hogar
        {
            'name': 'Cafetera Nespresso',
            'description': 'Máquina de café en cápsulas con 19 bares de presión',
            'price': Decimal('199.00'),
            'category': categories[2],
            'stock': 35,
            'is_active': True,
            'created_by': users[3]
        },
        {
            'name': 'Aspiradora Dyson V15',
            'description': 'Aspiradora inalámbrica con detección de partículas',
            'price': Decimal('549.99'),
            'category': categories[2],
            'stock': 20,
            'is_active': True,
            'created_by': users[1]
        },
        {
            'name': 'Lámpara LED Inteligente',
            'description': 'Bombilla LED WiFi compatible con Alexa y Google Home',
            'price': Decimal('24.99'),
            'category': categories[2],
            'stock': 150,
            'is_active': True,
            'created_by': users[2]
        },

        # Libros
        {
            'name': 'Clean Code - Robert Martin',
            'description': 'Libro sobre buenas prácticas de programación',
            'price': Decimal('39.99'),
            'category': categories[3],
            'stock': 45,
            'is_active': True,
            'created_by': users[3]
        },
        {
            'name': 'Python Crash Course',
            'description': 'Guía práctica para aprender Python desde cero',
            'price': Decimal('34.99'),
            'category': categories[3],
            'stock': 60,
            'is_active': True,
            'created_by': users[3]
        },
        {
            'name': 'El Señor de los Anillos',
            'description': 'Trilogía completa de J.R.R. Tolkien, edición especial',
            'price': Decimal('49.99'),
            'category': categories[3],
            'stock': 3,  # Stock bajo
            'is_active': True,
            'created_by': users[2]
        },

        # Deportes
        {
            'name': 'Bicicleta de Montaña Trek',
            'description': 'Bicicleta MTB con suspensión completa, 29 pulgadas',
            'price': Decimal('1299.00'),
            'category': categories[4],
            'stock': 12,
            'is_active': True,
            'created_by': users[1]
        },
        {
            'name': 'Mancuernas Ajustables 20kg',
            'description': 'Set de mancuernas con peso ajustable de 2.5 a 20kg',
            'price': Decimal('159.99'),
            'category': categories[4],
            'stock': 25,
            'is_active': True,
            'created_by': users[2]
        },
        {
            'name': 'Esterilla de Yoga',
            'description': 'Colchoneta antideslizante de 6mm con bolsa de transporte',
            'price': Decimal('29.99'),
            'category': categories[4],
            'stock': 80,
            'is_active': True,
            'created_by': users[3]
        },

        # Alimentos
        {
            'name': 'Café Colombiano Premium 1kg',
            'description': 'Café de grano entero, tueste medio, origen único',
            'price': Decimal('24.99'),
            'category': categories[5],
            'stock': 100,
            'is_active': True,
            'created_by': users[1]
        },
        {
            'name': 'Aceite de Oliva Extra Virgen',
            'description': 'Aceite de oliva español, primera prensada en frío, 1L',
            'price': Decimal('18.99'),
            'category': categories[5],
            'stock': 50,
            'is_active': True,
            'created_by': users[2]
        },
        {
            'name': 'Chocolate Belga 70% Cacao',
            'description': 'Tableta de chocolate negro premium, 200g',
            'price': Decimal('8.99'),
            'category': categories[5],
            'stock': 200,
            'is_active': True,
            'created_by': users[3]
        },

        # Productos inactivos para pruebas
        {
            'name': 'Producto Descontinuado',
            'description': 'Este producto ya no está disponible',
            'price': Decimal('99.99'),
            'category': categories[0],
            'stock': 0,
            'is_active': False,
            'created_by': users[1]
        },
    ]

    products = []
    for prod_data in products_data:
        product = Product.objects.create(**prod_data)
        products.append(product)
        status = "✓" if product.is_active else "✗"
        stock_warning = " ⚠️ STOCK BAJO" if product.stock < 10 and product.is_active else ""
        print(f"  {status} Producto creado: {product.name} - ${product.price}{stock_warning}")

    return products


def print_summary(users, categories, products):
    """Imprimir resumen de datos creados"""
    print("\n" + "="*60)
    print("📊 RESUMEN DE DATOS CREADOS")
    print("="*60)
    print(f"👥 Usuarios: {len(users)}")
    print(f"📁 Categorías: {len(categories)}")
    print(f"📦 Productos: {len(products)}")
    print(f"   - Activos: {sum(1 for p in products if p.is_active)}")
    print(f"   - Inactivos: {sum(1 for p in products if not p.is_active)}")
    print(f"   - Stock bajo (<10): {sum(1 for p in products if p.stock < 10 and p.is_active)}")
    print("="*60)
    print("\n✅ Base de datos poblada exitosamente!")
    print("\n📝 Credenciales de acceso:")
    print("   Admin: admin / admin123")
    print("   Usuario: juan / password123")
    print("   Usuario: maria / password123")
    print("   Usuario: carlos / password123")
    print("\n🌐 Accede a:")
    print("   API: http://localhost:8000/api/")
    print("   Admin: http://localhost:8000/admin/")
    print("="*60 + "\n")


def main():
    """Función principal"""
    print("\n" + "="*60)
    print("🚀 POBLANDO BASE DE DATOS")
    print("="*60)

    try:
        # Preguntar si limpiar datos existentes
        if Product.objects.exists() or Category.objects.exists():
            response = input("\n⚠️  Hay datos existentes. ¿Desea limpiarlos? (s/n): ")
            if response.lower() == 's':
                clear_data()
            else:
                print("Cancelando operación...")
                return

        # Crear datos
        users = create_users()
        categories = create_categories()
        products = create_products(categories, users)

        # Mostrar resumen
        print_summary(users, categories, products)

    except Exception as e:
        print(f"\n❌ Error al poblar la base de datos: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
