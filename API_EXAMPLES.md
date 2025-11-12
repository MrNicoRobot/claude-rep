# Ejemplos de Consultas CRUD - API REST

Este documento contiene ejemplos detallados de todas las operaciones CRUD disponibles en la API.

## Tabla de Contenidos

- [Categorías](#categorías)
- [Productos](#productos)
- [Usuarios](#usuarios)
- [Ejemplos con Python](#ejemplos-con-python)

---

## Categorías

### CREATE - Crear una categoría

**cURL:**
```bash
curl -X POST http://localhost:8000/api/categories/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Electrónica",
    "description": "Productos electrónicos y tecnología"
  }'
```

**Python requests:**
```python
import requests

url = "http://localhost:8000/api/categories/"
data = {
    "name": "Electrónica",
    "description": "Productos electrónicos y tecnología"
}
response = requests.post(url, json=data)
print(response.json())
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "name": "Electrónica",
  "description": "Productos electrónicos y tecnología",
  "products_count": 0,
  "created_at": "2025-11-12T10:00:00Z",
  "updated_at": "2025-11-12T10:00:00Z"
}
```

### READ - Listar todas las categorías

**cURL:**
```bash
curl -X GET http://localhost:8000/api/categories/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/categories/")
print(response.json())
```

### READ - Obtener una categoría específica

**cURL:**
```bash
curl -X GET http://localhost:8000/api/categories/1/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/categories/1/")
print(response.json())
```

### UPDATE - Actualizar una categoría (PUT - completo)

**cURL:**
```bash
curl -X PUT http://localhost:8000/api/categories/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Electrónica Avanzada",
    "description": "Productos electrónicos de última generación"
  }'
```

**Python requests:**
```python
url = "http://localhost:8000/api/categories/1/"
data = {
    "name": "Electrónica Avanzada",
    "description": "Productos electrónicos de última generación"
}
response = requests.put(url, json=data)
print(response.json())
```

### UPDATE - Actualizar una categoría (PATCH - parcial)

**cURL:**
```bash
curl -X PATCH http://localhost:8000/api/categories/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Nueva descripción actualizada"
  }'
```

**Python requests:**
```python
url = "http://localhost:8000/api/categories/1/"
data = {"description": "Nueva descripción actualizada"}
response = requests.patch(url, json=data)
print(response.json())
```

### DELETE - Eliminar una categoría

**cURL:**
```bash
curl -X DELETE http://localhost:8000/api/categories/1/
```

**Python requests:**
```python
response = requests.delete("http://localhost:8000/api/categories/1/")
print(response.status_code)  # Debería ser 204
```

### CUSTOM - Obtener productos de una categoría

**cURL:**
```bash
curl -X GET http://localhost:8000/api/categories/1/products/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/categories/1/products/")
print(response.json())
```

---

## Productos

### CREATE - Crear un producto

**cURL:**
```bash
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop Dell XPS 15",
    "description": "Laptop de alto rendimiento con procesador Intel i7",
    "price": 1299.99,
    "category": 1,
    "stock": 50,
    "is_active": true
  }'
```

**Python requests:**
```python
url = "http://localhost:8000/api/products/"
data = {
    "name": "Laptop Dell XPS 15",
    "description": "Laptop de alto rendimiento con procesador Intel i7",
    "price": 1299.99,
    "category": 1,
    "stock": 50,
    "is_active": True
}
response = requests.post(url, json=data)
print(response.json())
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "name": "Laptop Dell XPS 15",
  "description": "Laptop de alto rendimiento con procesador Intel i7",
  "price": "1299.99",
  "category": 1,
  "category_name": "Electrónica",
  "stock": 50,
  "is_active": true,
  "created_by": null,
  "created_by_username": null,
  "created_at": "2025-11-12T10:05:00Z",
  "updated_at": "2025-11-12T10:05:00Z"
}
```

### READ - Listar todos los productos

**cURL:**
```bash
curl -X GET http://localhost:8000/api/products/
```

**Con paginación:**
```bash
curl -X GET "http://localhost:8000/api/products/?page=1"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/")
print(response.json())
```

### READ - Obtener un producto específico

**cURL:**
```bash
curl -X GET http://localhost:8000/api/products/1/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/1/")
print(response.json())
```

### UPDATE - Actualizar un producto (PUT - completo)

**cURL:**
```bash
curl -X PUT http://localhost:8000/api/products/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop Dell XPS 15 - Actualizado",
    "description": "Laptop de alto rendimiento con Intel i9",
    "price": 1499.99,
    "category": 1,
    "stock": 45,
    "is_active": true
  }'
```

**Python requests:**
```python
url = "http://localhost:8000/api/products/1/"
data = {
    "name": "Laptop Dell XPS 15 - Actualizado",
    "description": "Laptop de alto rendimiento con Intel i9",
    "price": 1499.99,
    "category": 1,
    "stock": 45,
    "is_active": True
}
response = requests.put(url, json=data)
print(response.json())
```

### UPDATE - Actualizar un producto (PATCH - parcial)

**cURL:**
```bash
curl -X PATCH http://localhost:8000/api/products/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1199.99,
    "stock": 40
  }'
```

**Python requests:**
```python
url = "http://localhost:8000/api/products/1/"
data = {"price": 1199.99, "stock": 40}
response = requests.patch(url, json=data)
print(response.json())
```

### DELETE - Eliminar un producto

**cURL:**
```bash
curl -X DELETE http://localhost:8000/api/products/1/
```

**Python requests:**
```python
response = requests.delete("http://localhost:8000/api/products/1/")
print(response.status_code)  # Debería ser 204
```

---

## Filtros y Búsquedas en Productos

### Buscar productos por nombre o descripción

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/products/?search=laptop"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/?search=laptop")
print(response.json())
```

### Filtrar por categoría

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/products/?category=1"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/?category=1")
print(response.json())
```

### Filtrar por estado activo

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/products/?is_active=true"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/?is_active=true")
print(response.json())
```

### Ordenar por precio (ascendente)

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/products/?ordering=price"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/?ordering=price")
print(response.json())
```

### Ordenar por precio (descendente)

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/products/?ordering=-price"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/?ordering=-price")
print(response.json())
```

### Combinar múltiples filtros

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/products/?category=1&is_active=true&ordering=-price&search=laptop"
```

**Python requests:**
```python
params = {
    "category": 1,
    "is_active": "true",
    "ordering": "-price",
    "search": "laptop"
}
response = requests.get("http://localhost:8000/api/products/", params=params)
print(response.json())
```

---

## Endpoints Personalizados de Productos

### Obtener solo productos activos

**cURL:**
```bash
curl -X GET http://localhost:8000/api/products/active/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/active/")
print(response.json())
```

### Obtener productos con stock bajo (< 10 unidades)

**cURL:**
```bash
curl -X GET http://localhost:8000/api/products/low_stock/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/products/low_stock/")
print(response.json())
```

### Alternar estado activo/inactivo de un producto

**cURL:**
```bash
curl -X POST http://localhost:8000/api/products/1/toggle_active/
```

**Python requests:**
```python
response = requests.post("http://localhost:8000/api/products/1/toggle_active/")
print(response.json())
```

---

## Usuarios

### READ - Listar todos los usuarios

**cURL:**
```bash
curl -X GET http://localhost:8000/api/users/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/users/")
print(response.json())
```

### READ - Obtener un usuario específico

**cURL:**
```bash
curl -X GET http://localhost:8000/api/users/1/
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/users/1/")
print(response.json())
```

### Buscar usuarios

**cURL:**
```bash
curl -X GET "http://localhost:8000/api/users/?search=john"
```

**Python requests:**
```python
response = requests.get("http://localhost:8000/api/users/?search=john")
print(response.json())
```

---

## Ejemplos con Python

### Script completo de ejemplo

```python
import requests
import json

BASE_URL = "http://localhost:8000/api"

def pretty_print(data):
    """Imprimir JSON de forma legible"""
    print(json.dumps(data, indent=2))

# 1. CREAR CATEGORÍA
print("=== CREANDO CATEGORÍA ===")
category_data = {
    "name": "Electrónica",
    "description": "Productos electrónicos y gadgets"
}
response = requests.post(f"{BASE_URL}/categories/", json=category_data)
category = response.json()
pretty_print(category)
category_id = category['id']

# 2. LISTAR CATEGORÍAS
print("\n=== LISTANDO CATEGORÍAS ===")
response = requests.get(f"{BASE_URL}/categories/")
pretty_print(response.json())

# 3. CREAR PRODUCTO
print("\n=== CREANDO PRODUCTO ===")
product_data = {
    "name": "iPhone 15 Pro",
    "description": "Smartphone de última generación",
    "price": 999.99,
    "category": category_id,
    "stock": 100,
    "is_active": True
}
response = requests.post(f"{BASE_URL}/products/", json=product_data)
product = response.json()
pretty_print(product)
product_id = product['id']

# 4. OBTENER PRODUCTO ESPECÍFICO
print("\n=== OBTENIENDO PRODUCTO ===")
response = requests.get(f"{BASE_URL}/products/{product_id}/")
pretty_print(response.json())

# 5. ACTUALIZAR PRODUCTO (PATCH)
print("\n=== ACTUALIZANDO PRODUCTO ===")
update_data = {
    "price": 899.99,
    "stock": 95
}
response = requests.patch(f"{BASE_URL}/products/{product_id}/", json=update_data)
pretty_print(response.json())

# 6. BUSCAR PRODUCTOS
print("\n=== BUSCANDO PRODUCTOS ===")
response = requests.get(f"{BASE_URL}/products/?search=iphone")
pretty_print(response.json())

# 7. FILTRAR PRODUCTOS POR CATEGORÍA
print("\n=== FILTRANDO POR CATEGORÍA ===")
response = requests.get(f"{BASE_URL}/products/?category={category_id}")
pretty_print(response.json())

# 8. OBTENER PRODUCTOS ACTIVOS
print("\n=== PRODUCTOS ACTIVOS ===")
response = requests.get(f"{BASE_URL}/products/active/")
pretty_print(response.json())

# 9. ALTERNAR ESTADO DEL PRODUCTO
print("\n=== ALTERNANDO ESTADO ===")
response = requests.post(f"{BASE_URL}/products/{product_id}/toggle_active/")
pretty_print(response.json())

# 10. OBTENER PRODUCTOS DE UNA CATEGORÍA
print("\n=== PRODUCTOS DE CATEGORÍA ===")
response = requests.get(f"{BASE_URL}/categories/{category_id}/products/")
pretty_print(response.json())

# 11. ELIMINAR PRODUCTO (comentado para no borrar datos)
# print("\n=== ELIMINANDO PRODUCTO ===")
# response = requests.delete(f"{BASE_URL}/products/{product_id}/")
# print(f"Status code: {response.status_code}")

print("\n=== COMPLETADO ===")
```

### Clase helper para operaciones CRUD

```python
import requests
from typing import Dict, List, Optional

class APIClient:
    """Cliente para interactuar con la API"""

    def __init__(self, base_url: str = "http://localhost:8000/api"):
        self.base_url = base_url
        self.session = requests.Session()

    # CATEGORÍAS
    def create_category(self, name: str, description: str = "") -> Dict:
        """Crear una nueva categoría"""
        data = {"name": name, "description": description}
        response = self.session.post(f"{self.base_url}/categories/", json=data)
        response.raise_for_status()
        return response.json()

    def get_categories(self, search: Optional[str] = None) -> Dict:
        """Obtener todas las categorías"""
        params = {"search": search} if search else {}
        response = self.session.get(f"{self.base_url}/categories/", params=params)
        response.raise_for_status()
        return response.json()

    def get_category(self, category_id: int) -> Dict:
        """Obtener una categoría específica"""
        response = self.session.get(f"{self.base_url}/categories/{category_id}/")
        response.raise_for_status()
        return response.json()

    def update_category(self, category_id: int, **kwargs) -> Dict:
        """Actualizar una categoría (parcial)"""
        response = self.session.patch(f"{self.base_url}/categories/{category_id}/", json=kwargs)
        response.raise_for_status()
        return response.json()

    def delete_category(self, category_id: int) -> bool:
        """Eliminar una categoría"""
        response = self.session.delete(f"{self.base_url}/categories/{category_id}/")
        return response.status_code == 204

    # PRODUCTOS
    def create_product(self, name: str, description: str, price: float,
                      category_id: int, stock: int = 0, is_active: bool = True) -> Dict:
        """Crear un nuevo producto"""
        data = {
            "name": name,
            "description": description,
            "price": price,
            "category": category_id,
            "stock": stock,
            "is_active": is_active
        }
        response = self.session.post(f"{self.base_url}/products/", json=data)
        response.raise_for_status()
        return response.json()

    def get_products(self, **filters) -> Dict:
        """Obtener productos con filtros opcionales"""
        response = self.session.get(f"{self.base_url}/products/", params=filters)
        response.raise_for_status()
        return response.json()

    def get_product(self, product_id: int) -> Dict:
        """Obtener un producto específico"""
        response = self.session.get(f"{self.base_url}/products/{product_id}/")
        response.raise_for_status()
        return response.json()

    def update_product(self, product_id: int, **kwargs) -> Dict:
        """Actualizar un producto (parcial)"""
        response = self.session.patch(f"{self.base_url}/products/{product_id}/", json=kwargs)
        response.raise_for_status()
        return response.json()

    def delete_product(self, product_id: int) -> bool:
        """Eliminar un producto"""
        response = self.session.delete(f"{self.base_url}/products/{product_id}/")
        return response.status_code == 204

    def get_active_products(self) -> Dict:
        """Obtener solo productos activos"""
        response = self.session.get(f"{self.base_url}/products/active/")
        response.raise_for_status()
        return response.json()

    def get_low_stock_products(self) -> Dict:
        """Obtener productos con stock bajo"""
        response = self.session.get(f"{self.base_url}/products/low_stock/")
        response.raise_for_status()
        return response.json()

    def toggle_product_active(self, product_id: int) -> Dict:
        """Alternar estado activo/inactivo"""
        response = self.session.post(f"{self.base_url}/products/{product_id}/toggle_active/")
        response.raise_for_status()
        return response.json()

# Ejemplo de uso
if __name__ == "__main__":
    client = APIClient()

    # Crear categoría
    category = client.create_category("Libros", "Libros y publicaciones")
    print(f"Categoría creada: {category['name']}")

    # Crear producto
    product = client.create_product(
        name="Python Programming",
        description="Libro de programación en Python",
        price=29.99,
        category_id=category['id'],
        stock=50
    )
    print(f"Producto creado: {product['name']}")

    # Buscar productos
    results = client.get_products(search="python", ordering="-price")
    print(f"Productos encontrados: {results['count']}")

    # Actualizar stock
    updated = client.update_product(product['id'], stock=45)
    print(f"Stock actualizado: {updated['stock']}")
```

---

## Códigos de Respuesta HTTP

- **200 OK**: Operación exitosa (GET, PUT, PATCH)
- **201 Created**: Recurso creado exitosamente (POST)
- **204 No Content**: Recurso eliminado exitosamente (DELETE)
- **400 Bad Request**: Datos inválidos
- **404 Not Found**: Recurso no encontrado
- **500 Internal Server Error**: Error del servidor

---

## Notas Importantes

1. Todos los endpoints soportan formato JSON
2. La paginación está habilitada por defecto (10 items por página)
3. Los filtros se pueden combinar usando `&` en la URL
4. Para ordenar de forma descendente, usa `-` antes del nombre del campo
5. Las búsquedas no distinguen entre mayúsculas y minúsculas
6. Los campos `created_at` y `updated_at` se generan automáticamente
