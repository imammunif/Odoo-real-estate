from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "This name was already taken, please choose others")
    ]

    name = fields.Char(string="Name", required=True)
