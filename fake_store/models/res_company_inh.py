from odoo import models, fields

class ResCompanyInh(models.Model):
    _inherit = 'res.company'

    fake_store_api_key = fields.Char(string="Credenciales API")
    fake_store_api_active = fields.Boolean(string="Activar API", default=False)
