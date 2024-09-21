from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate property tag"

    name = fields.Char(string="Name", required=True)
