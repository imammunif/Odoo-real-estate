from email.policy import default

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer"
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The price must be strictly positive")
    ]

    price = fields.Char(string="Price", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
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

    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    # ----------------------------------------- Action Methods ----------------------------------------

    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.state"):
            raise UserError("An offer as already been accepted.")
        self.write(
            {
                "state": "accepted",
            }
        )
        return self.mapped("property_id").write(
            {
                "state": "offer_accepted",
                "selling_price": self.price,
                "buyer_id": self.partner_id.id,
            }
        )

    def action_refuse(self):
        return self.write(
            {
                "state": "refused"
            }
        )
