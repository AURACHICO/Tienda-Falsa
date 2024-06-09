# Integracion de API Fake Store 

Este módulo integra productos de la Fake Store API en Odoo.

## Características

- Crea nuevos productos si no existen previamente.
- Actualiza productos existentes con la información más reciente de la API.
- Actualiza los productos diariamente de manera automatizada.
- Las credenciales de la API son configurables desde los ajustes de la compañía.
- Permite activar o desactivar el uso de la API.
- Los productos se crean o actualizan con todos los datos que retorna la API.
- La imagen del producto se carga utilizando la URL proporcionada por la API.
- Permite exportar la lista de productos a un archivo de Excel.

## Instalación

1. Asegúrate de tener todas las dependencias instaladas. Abre una terminal y navega hasta el directorio raíz de tu instalación de Odoo. Luego, ejecuta el siguiente comando:
- cd server
- pip install -r requirements.txt

2. Una vez configurado Odoo, puedes usar el comando scaffold para crear la estructura básica de tu nuevo módulo. Abre una terminal y ejecuta el siguiente comando:
- python 'C:\Program Files\Odoo 17.0\server\odoo-bin' scaffold fake_store
Esto creará automáticamente la estructura básica del módulo.


## Configuración

1. Configurar el archivo 'odoo.conf':
- db_user: El nombre de usuario de la base de datos que creaste en PostgreSQL.
- pg_path: La ruta donde está alojado tu gestor de base de datos PostgreSQL.
- db_password: La contraseña de la base de datos que agregaste al crear el usuario de la base de datos.
- addons_path: La ruta a la carpeta donde realizarás tus modificaciones (por ejemplo, tus nuevos módulos: C:\Program Files\Odoo 17.0\server\odoo-bin).

2. Ejecutar Odoo con este comando:
- python odoo-bin


## Uso

1. Ir a Ajustes de la compañía y colocar las credenciales y activar el uso de la API.
2. Los productos se actualizan automáticamente todos los días (Para esto se creo una accion planeada: Actualizar Productos).
3. Para exportar los productos a un archivo de Excel, hacer clic en el botón "Exportar Productos" en el sitio web de Odoo.
4. Tambien puedes exportar el archivo de Excel por esta ruta : http://localhost:8069/exportar_productos
