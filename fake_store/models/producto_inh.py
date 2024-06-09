import base64
import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductTemplateInh(models.Model):
    _inherit = 'product.template'

    #  campos adicionales para alamecenar informacion
    fake_store_id = fields.Integer(string="ID de Tienda")
    fake_store_category = fields.Char(string="Categoria")
    fake_store_rating = fields.Float(string="Clasificación")
    fake_store_rating_count = fields.Integer(string="Recuento de calificaciones")

    @api.model
    def update_products_from_fake_store(self):
        # Obtenemos la compañía del usuario actual
        company = self.env.user.company_id
        # Verificamos si la API esta activa
        if not company.fake_store_api_active or not company.fake_store_api_key:
            raise UserError('Las credenciales de la API de Fake Store no están configuradas correctamente')


        # URL de la API de Fake Store
        url = 'https://fakestoreapi.com/products'

        # Realizamos una solicitud GET a la API
        response = requests.get(url)
        # Verificamos si la solicitud fue exitosa
        if response.status_code != 200:
            raise UserError('Error al obtener datos de la API')

        # Convertimos la respuesta JSON en una lista de productos 
        products = response.json()
        for product in products:
            # Buscamos si el producto ya existe en Odoo por su ID de tienda
            existing_product = self.search([('fake_store_id', '=', product['id'])], limit=1)

            # Preparamos los datos del producto para crear o actualizar el registro en Odoo
            product_data = {
                'name': product['title'],
                'list_price': product['price'],
                'description_sale': product['description'],
                'image_1920': self._get_image_from_url(product['image']),
                'fake_store_id': product['id'],
                'fake_store_category': product['category'],
                'fake_store_rating': product['rating']['rate'],
                'fake_store_rating_count': product['rating']['count'],
            }
            # Si el producto ya existe, lo actualizamos; de lo contrario, lo creamos
            if existing_product:
                existing_product.write(product_data)
            else:
                self.create(product_data)

    def _get_image_from_url(self, url):
        # Descargamos la imagen desde la URL y la codificamos en formato base64
        response = requests.get(url)
        if response.status_code == 200:
            return base64.b64encode(response.content)
        return False
