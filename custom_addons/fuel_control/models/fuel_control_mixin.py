from odoo import models, fields, api


class FuelControlMixin(models.AbstractModel):
    _name = "fuel.control.mixin"
    _description = "Fuel Control Mixin"

    date = fields.Datetime(
        string="Date and Time",
        default=fields.Datetime.now,
        required=True
    )

    liters = fields.Float(
        string="Liters",
        required=True
    )

    price_per_liter = fields.Float(
        string="Price per Liter",
        required=True
    )

    total_amount = fields.Float(
        string="Total",
        compute="_compute_total",
        store=True
    )

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible User",
        default=lambda self: self.env.user,
        readonly=True,
    )

    @api.depends("liters", "price_per_liter")
    def _compute_total(self):
        for rec in self:
            rec.total_amount = rec.liters * rec.price_per_liter
