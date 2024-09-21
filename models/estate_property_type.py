from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type"

    name = fields.Char(string="Name", required=True)
