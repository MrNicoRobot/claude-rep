# Backend Django REST Framework

Backend API RESTful construido con Django y Django REST Framework, que proporciona un sistema completo de gestión de productos y categorías.

## Características

- API RESTful completa con operaciones CRUD
- Sistema de autenticación integrado
- Filtrado, búsqueda y ordenamiento avanzado
- Paginación automática
- Panel de administración de Django
- Validaciones de datos
- CORS configurado para desarrollo frontend
- Documentación de API navegable

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd claude-rep
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **(Opcional) Poblar la base de datos con datos de prueba:**
```bash
python populate_db.py
```

Este script creará automáticamente:
- Un superusuario (admin / admin123)
- 3 usuarios de prueba
- 6 categorías de productos
- 20+ productos de ejemplo

6. **(Alternativa) Crear un superusuario manualmente:**
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000`

## Endpoints API

### Categorías

- `GET /api/categories/` - Listar todas las categorías
- `POST /api/categories/` - Crear una nueva categoría
- `GET /api/categories/{id}/` - Obtener una categoría específica
- `PUT /api/categories/{id}/` - Actualizar una categoría
- `PATCH /api/categories/{id}/` - Actualizar parcialmente una categoría
- `DELETE /api/categories/{id}/` - Eliminar una categoría
- `GET /api/categories/{id}/products/` - Obtener todos los productos de una categoría

### Productos

- `GET /api/products/` - Listar todos los productos
- `POST /api/products/` - Crear un nuevo producto
- `GET /api/products/{id}/` - Obtener un producto específico
- `PUT /api/products/{id}/` - Actualizar un producto
- `PATCH /api/products/{id}/` - Actualizar parcialmente un producto
- `DELETE /api/products/{id}/` - Eliminar un producto
- `GET /api/products/active/` - Obtener solo productos activos
- `GET /api/products/low_stock/` - Obtener productos con stock bajo
- `POST /api/products/{id}/toggle_active/` - Alternar estado activo/inactivo

### Usuarios

- `GET /api/users/` - Listar todos los usuarios
- `GET /api/users/{id}/` - Obtener un usuario específico

## Filtros y Búsqueda

### Productos

Búsqueda por nombre o descripción:
```
GET /api/products/?search=laptop
```

Filtrar por categoría:
```
GET /api/products/?category=1
```

Filtrar por estado activo:
```
GET /api/products/?is_active=true
```

Ordenar por precio:
```
GET /api/products/?ordering=price
GET /api/products/?ordering=-price  # Descendente
```

Combinar filtros:
```
GET /api/products/?category=1&is_active=true&ordering=-created_at
```

## Estructura del Proyecto

```
claude-rep/
├── backend/              # Configuración del proyecto Django
│   ├── settings.py      # Configuraciones principales
│   ├── urls.py          # URLs principales
│   ├── wsgi.py          # Punto de entrada WSGI
│   └── asgi.py          # Punto de entrada ASGI
├── api/                  # Aplicación principal de la API
│   ├── models.py        # Modelos de datos
│   ├── serializers.py   # Serializadores DRF
│   ├── views.py         # Vistas y ViewSets
│   ├── urls.py          # URLs de la API
│   └── admin.py         # Configuración del admin
├── manage.py            # Script de gestión de Django
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Este archivo
```

## Modelos

### Category
- `name`: Nombre de la categoría (único)
- `description`: Descripción de la categoría
- `created_at`: Fecha de creación
- `updated_at`: Fecha de última actualización

### Product
- `name`: Nombre del producto
- `description`: Descripción del producto
- `price`: Precio del producto
- `category`: Categoría del producto (ForeignKey)
- `stock`: Cantidad en stock
- `is_active`: Estado activo/inactivo
- `created_by`: Usuario que creó el producto (ForeignKey)
- `created_at`: Fecha de creación
- `updated_at`: Fecha de última actualización

## Panel de Administración

Accede al panel de administración en `http://localhost:8000/admin/` usando las credenciales del superusuario.

Desde aquí puedes:
- Gestionar usuarios
- Crear, editar y eliminar categorías
- Crear, editar y eliminar productos
- Ver estadísticas y filtrar datos

## API Navegable

Django REST Framework proporciona una interfaz web navegable para la API. Accede a `http://localhost:8000/api/` para explorar los endpoints de forma interactiva.

## Configuración de CORS

El backend está configurado para aceptar peticiones desde:
- `http://localhost:3000`
- `http://localhost:8080`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:8080`

Para añadir más orígenes, edita `CORS_ALLOWED_ORIGINS` en `backend/settings.py`.

## Validaciones

El backend incluye validaciones automáticas:
- El precio no puede ser negativo
- El stock no puede ser negativo
- Los nombres de categorías deben ser únicos
- Campos requeridos validados automáticamente

## Tecnologías Utilizadas

- **Django 5.0**: Framework web de Python
- **Django REST Framework 3.14+**: Toolkit para construir Web APIs
- **django-cors-headers**: Manejo de CORS
- **django-filter**: Sistema de filtrado avanzado
- **psycopg2-binary**: Adaptador de PostgreSQL (para producción)
- **python-decouple**: Gestión de configuración

## Testing y Pruebas

### Ejecutar Tests

El proyecto incluye tests completos para todas las operaciones CRUD:

```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests de una app específica
python manage.py test api

# Ejecutar con más detalles
python manage.py test --verbosity=2

# Ejecutar tests específicos
python manage.py test api.tests.ProductAPITest
```

Los tests cubren:
- ✅ Modelos (Category, Product)
- ✅ API CRUD completo (CREATE, READ, UPDATE, DELETE)
- ✅ Validaciones (precios/stock negativos)
- ✅ Filtros y búsquedas
- ✅ Paginación
- ✅ Endpoints personalizados

### Documentación de Consultas CRUD

📚 **Consulta el archivo `API_EXAMPLES.md`** para ver ejemplos completos de:
- Consultas con **cURL**
- Scripts con **Python requests**
- Clase helper reutilizable para el cliente API
- Ejemplos de filtros, búsquedas y ordenamiento
- Todos los endpoints disponibles

### Colección Postman

📮 Importa el archivo `postman_collection.json` en Postman o Thunder Client para:
- Probar todos los endpoints CRUD
- Ejemplos pre-configurados
- Variables de entorno
- Requests organizados por recurso

### Poblar Base de Datos

Para añadir datos de prueba de forma rápida:

```bash
python populate_db.py
```

El script te preguntará si quieres limpiar datos existentes y creará:
- **Usuarios**: admin, juan, maria, carlos
- **Categorías**: Electrónica, Ropa, Hogar, Libros, Deportes, Alimentos
- **Productos**: 20+ productos con datos realistas
- **Productos especiales**: Algunos con stock bajo, productos inactivos

## Desarrollo

Para crear migraciones después de cambios en los modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Archivos del Proyecto

```
claude-rep/
├── API_EXAMPLES.md          # 📚 Documentación completa de consultas CRUD
├── postman_collection.json  # 📮 Colección Postman/Thunder Client
├── populate_db.py           # 🗄️ Script para poblar base de datos
├── requirements.txt         # 📦 Dependencias
├── manage.py               # 🔧 Utilidad de gestión Django
├── backend/                # ⚙️ Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── api/                    # 🚀 Aplicación principal
    ├── models.py           # Modelos Category y Product
    ├── serializers.py      # Serializadores DRF
    ├── views.py            # ViewSets y endpoints
    ├── urls.py             # Rutas de la API
    ├── admin.py            # Panel de administración
    └── tests.py            # 🧪 Tests completos CRUD
```

## Próximos Pasos

Sugerencias para expandir el backend:

1. Añadir autenticación JWT con `djangorestframework-simplejwt`
2. Implementar permisos más granulares
3. Añadir sistema de imágenes para productos
4. Implementar sistema de órdenes y carritos de compra
5. Añadir tests unitarios e integración
6. Configurar PostgreSQL para producción
7. Añadir documentación con Swagger/OpenAPI
8. Implementar caché con Redis
9. Añadir sistema de notificaciones
10. Implementar webhooks

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
