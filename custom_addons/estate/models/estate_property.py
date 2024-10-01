from odoo import fields, models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'ESTATE Properties'

    name = fields.Char(string="Title", required=True, help="Property name")
