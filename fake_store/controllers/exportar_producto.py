import xlsxwriter
from odoo import http
from odoo.http import request
import io

class ExportProductsController(http.Controller):

    @http.route('/exportar_productos', type='http', auth='user')
    def export_fake_store_products(self):
        # Obtenemos todos los productos que tienen un ID de tienda de Fake Store asignado
        products = request.env['product.template'].search([('fake_store_id', '!=', False)])

        # Creamos un archivo Excel en memoria
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        # Escribimos los encabezados de las columnas en el archivo Excel
        headers = ['ID', 'Nombre', 'Precio', 'Descripcion', 'Categoria', 'Clasificación', 'Recuento de calificaciones']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header)

        # Escribimos los datos de los productos en el archivo Excel
        row_num = 1
        for product in products:
            worksheet.write(row_num, 0, product.fake_store_id)
            worksheet.write(row_num, 1, product.name)
            worksheet.write(row_num, 2, product.list_price)
            worksheet.write(row_num, 3, product.description)
            worksheet.write(row_num, 4, product.fake_store_category)
            worksheet.write(row_num, 5, product.fake_store_rating)
            worksheet.write(row_num, 6, product.fake_store_rating_count)
            row_num += 1

        # Cerramos el archivo Excel y lo retornamos como una respuesta HTTP para su descarga
        workbook.close()
        output.seek(0)
        return request.make_response(output.read(),
                                     headers=[
                                         ('Content-Disposition', 'attachment; filename="fake_store_productos.xlsx"'),
                                         ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                                     ])
