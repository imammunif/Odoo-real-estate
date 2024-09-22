from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer"


    price = fields.Char(string="Price", required=True)
    state = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused")],
        string="Status",
        readonly=True,
        default=False
    )

    partner_id = fields.Many2one("res.partner", required=True, string="Partner")
    property_id = fields.Many2one("estate.property", required=True, string="Property")
