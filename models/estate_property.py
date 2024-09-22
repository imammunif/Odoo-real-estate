from email.policy import default

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property description"

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', default=lambda self: self._default_date_availability(), copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Float(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Float(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')],
        string='Garden Orientation')
    active = fields.Boolean(string="Active", default=False)
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer received"),
            ("offer_accepted", "Offer accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new"
    )

    # Relational fields
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")