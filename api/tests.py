from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from decimal import Decimal

from .models import Category, Product


class CategoryModelTest(TestCase):
    """Tests para el modelo Category"""

    def setUp(self):
        self.category = Category.objects.create(
            name="Electrónica",
            description="Productos electrónicos"
        )

    def test_category_creation(self):
        """Test de creación de categoría"""
        self.assertEqual(self.category.name, "Electrónica")
        self.assertEqual(self.category.description, "Productos electrónicos")
        self.assertIsNotNone(self.category.created_at)
        self.assertIsNotNone(self.category.updated_at)

    def test_category_str(self):
        """Test del método __str__"""
        self.assertEqual(str(self.category), "Electrónica")


class ProductModelTest(TestCase):
    """Tests para el modelo Product"""

    def setUp(self):
        self.category = Category.objects.create(
            name="Electrónica",
            description="Productos electrónicos"
        )
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.product = Product.objects.create(
            name="Laptop",
            description="Laptop de alta gama",
            price=Decimal("1299.99"),
            category=self.category,
            stock=10,
            is_active=True,
            created_by=self.user
        )

    def test_product_creation(self):
        """Test de creación de producto"""
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, Decimal("1299.99"))
        self.assertEqual(self.product.stock, 10)
        self.assertTrue(self.product.is_active)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.created_by, self.user)

    def test_product_str(self):
        """Test del método __str__"""
        self.assertEqual(str(self.product), "Laptop")


class CategoryAPITest(APITestCase):
    """Tests para el API de categorías"""

    def setUp(self):
        self.client = APIClient()
        self.category_data = {
            "name": "Libros",
            "description": "Libros y publicaciones"
        }

    def test_create_category(self):
        """Test CREATE - Crear categoría"""
        response = self.client.post('/api/categories/', self.category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "Libros")

    def test_list_categories(self):
        """Test READ - Listar categorías"""
        Category.objects.create(name="Cat1", description="Desc1")
        Category.objects.create(name="Cat2", description="Desc2")

        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_category(self):
        """Test READ - Obtener categoría específica"""
        category = Category.objects.create(name="Test", description="Test desc")

        response = self.client.get(f'/api/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test")

    def test_update_category(self):
        """Test UPDATE - Actualizar categoría con PUT"""
        category = Category.objects.create(name="Original", description="Desc")

        update_data = {
            "name": "Actualizado",
            "description": "Nueva descripción"
        }
        response = self.client.put(f'/api/categories/{category.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        category.refresh_from_db()
        self.assertEqual(category.name, "Actualizado")

    def test_partial_update_category(self):
        """Test UPDATE - Actualizar categoría con PATCH"""
        category = Category.objects.create(name="Original", description="Desc")

        update_data = {"description": "Descripción actualizada"}
        response = self.client.patch(f'/api/categories/{category.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        category.refresh_from_db()
        self.assertEqual(category.description, "Descripción actualizada")
        self.assertEqual(category.name, "Original")  # No cambió

    def test_delete_category(self):
        """Test DELETE - Eliminar categoría"""
        category = Category.objects.create(name="ToDelete", description="Desc")

        response = self.client.delete(f'/api/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_search_categories(self):
        """Test de búsqueda en categorías"""
        Category.objects.create(name="Electrónica", description="Gadgets")
        Category.objects.create(name="Libros", description="Publicaciones")

        response = self.client.get('/api/categories/?search=Electr')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_category_products_endpoint(self):
        """Test endpoint personalizado de productos por categoría"""
        category = Category.objects.create(name="Test", description="Test")
        Product.objects.create(
            name="Product1",
            description="Desc1",
            price=Decimal("10.00"),
            category=category,
            stock=5
        )

        response = self.client.get(f'/api/categories/{category.id}/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ProductAPITest(APITestCase):
    """Tests para el API de productos"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Electrónica",
            description="Productos electrónicos"
        )
        self.product_data = {
            "name": "iPhone 15",
            "description": "Smartphone Apple",
            "price": "999.99",
            "category": self.category.id,
            "stock": 50,
            "is_active": True
        }

    def test_create_product(self):
        """Test CREATE - Crear producto"""
        response = self.client.post('/api/products/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "iPhone 15")

    def test_create_product_with_negative_price(self):
        """Test validación de precio negativo"""
        invalid_data = self.product_data.copy()
        invalid_data['price'] = "-10.00"

        response = self.client.post('/api/products/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_product_with_negative_stock(self):
        """Test validación de stock negativo"""
        invalid_data = self.product_data.copy()
        invalid_data['stock'] = -5

        response = self.client.post('/api/products/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_products(self):
        """Test READ - Listar productos"""
        Product.objects.create(
            name="Product1",
            description="Desc1",
            price=Decimal("10.00"),
            category=self.category,
            stock=5
        )
        Product.objects.create(
            name="Product2",
            description="Desc2",
            price=Decimal("20.00"),
            category=self.category,
            stock=10
        )

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_product(self):
        """Test READ - Obtener producto específico"""
        product = Product.objects.create(
            name="Test Product",
            description="Test",
            price=Decimal("99.99"),
            category=self.category,
            stock=5
        )

        response = self.client.get(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Product")

    def test_update_product(self):
        """Test UPDATE - Actualizar producto con PUT"""
        product = Product.objects.create(
            name="Original",
            description="Desc",
            price=Decimal("100.00"),
            category=self.category,
            stock=10
        )

        update_data = {
            "name": "Actualizado",
            "description": "Nueva desc",
            "price": "150.00",
            "category": self.category.id,
            "stock": 15,
            "is_active": True
        }
        response = self.client.put(f'/api/products/{product.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product.refresh_from_db()
        self.assertEqual(product.name, "Actualizado")
        self.assertEqual(product.price, Decimal("150.00"))

    def test_partial_update_product(self):
        """Test UPDATE - Actualizar producto con PATCH"""
        product = Product.objects.create(
            name="Original",
            description="Desc",
            price=Decimal("100.00"),
            category=self.category,
            stock=10
        )

        update_data = {"price": "120.00", "stock": 8}
        response = self.client.patch(f'/api/products/{product.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product.refresh_from_db()
        self.assertEqual(product.price, Decimal("120.00"))
        self.assertEqual(product.stock, 8)
        self.assertEqual(product.name, "Original")  # No cambió

    def test_delete_product(self):
        """Test DELETE - Eliminar producto"""
        product = Product.objects.create(
            name="ToDelete",
            description="Desc",
            price=Decimal("50.00"),
            category=self.category,
            stock=5
        )

        response = self.client.delete(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_filter_by_category(self):
        """Test filtrado por categoría"""
        category2 = Category.objects.create(name="Libros", description="Books")

        Product.objects.create(
            name="Laptop",
            description="Computer",
            price=Decimal("1000.00"),
            category=self.category,
            stock=5
        )
        Product.objects.create(
            name="Python Book",
            description="Programming book",
            price=Decimal("30.00"),
            category=category2,
            stock=10
        )

        response = self.client.get(f'/api/products/?category={self.category.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_filter_by_active_status(self):
        """Test filtrado por estado activo"""
        Product.objects.create(
            name="Active Product",
            description="Active",
            price=Decimal("100.00"),
            category=self.category,
            stock=5,
            is_active=True
        )
        Product.objects.create(
            name="Inactive Product",
            description="Inactive",
            price=Decimal("200.00"),
            category=self.category,
            stock=5,
            is_active=False
        )

        response = self.client.get('/api/products/?is_active=true')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_products(self):
        """Test búsqueda de productos"""
        Product.objects.create(
            name="iPhone 15 Pro",
            description="Apple smartphone",
            price=Decimal("1200.00"),
            category=self.category,
            stock=10
        )
        Product.objects.create(
            name="Samsung Galaxy",
            description="Android smartphone",
            price=Decimal("900.00"),
            category=self.category,
            stock=15
        )

        response = self.client.get('/api/products/?search=iPhone')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_by_price(self):
        """Test ordenamiento por precio"""
        Product.objects.create(
            name="Cheap",
            description="Low price",
            price=Decimal("10.00"),
            category=self.category,
            stock=5
        )
        Product.objects.create(
            name="Expensive",
            description="High price",
            price=Decimal("1000.00"),
            category=self.category,
            stock=5
        )

        # Orden ascendente
        response = self.client.get('/api/products/?ordering=price')
        self.assertEqual(response.data['results'][0]['name'], "Cheap")

        # Orden descendente
        response = self.client.get('/api/products/?ordering=-price')
        self.assertEqual(response.data['results'][0]['name'], "Expensive")

    def test_active_products_endpoint(self):
        """Test endpoint de productos activos"""
        Product.objects.create(
            name="Active",
            description="Active product",
            price=Decimal("100.00"),
            category=self.category,
            stock=5,
            is_active=True
        )
        Product.objects.create(
            name="Inactive",
            description="Inactive product",
            price=Decimal("100.00"),
            category=self.category,
            stock=5,
            is_active=False
        )

        response = self.client.get('/api/products/active/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_low_stock_endpoint(self):
        """Test endpoint de productos con stock bajo"""
        Product.objects.create(
            name="High Stock",
            description="Много stock",
            price=Decimal("100.00"),
            category=self.category,
            stock=50,
            is_active=True
        )
        Product.objects.create(
            name="Low Stock",
            description="Low stock",
            price=Decimal("100.00"),
            category=self.category,
            stock=5,
            is_active=True
        )

        response = self.client.get('/api/products/low_stock/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Low Stock")

    def test_toggle_active_endpoint(self):
        """Test endpoint para alternar estado activo"""
        product = Product.objects.create(
            name="Test",
            description="Test",
            price=Decimal("100.00"),
            category=self.category,
            stock=5,
            is_active=True
        )

        # Alternar a inactivo
        response = self.client.post(f'/api/products/{product.id}/toggle_active/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertFalse(product.is_active)

        # Alternar de nuevo a activo
        response = self.client.post(f'/api/products/{product.id}/toggle_active/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertTrue(product.is_active)

    def test_pagination(self):
        """Test de paginación"""
        # Crear más de 10 productos (límite de página)
        for i in range(15):
            Product.objects.create(
                name=f"Product {i}",
                description=f"Description {i}",
                price=Decimal("10.00"),
                category=self.category,
                stock=5
            )

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)  # Página 1
        self.assertIsNotNone(response.data['next'])  # Hay página siguiente

        # Página 2
        response = self.client.get('/api/products/?page=2')
        self.assertEqual(len(response.data['results']), 5)  # Resto de productos
