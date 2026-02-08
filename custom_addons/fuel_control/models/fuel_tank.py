from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class FuelTank(models.Model):
    _name = "fuel.tank"
    _description = "Fuel Tank"
    _rec_name = "name"

    name = fields.Char(
        required=True,
    )
    code = fields.Char(
        required=True,
    )
    capacity_liters = fields.Float(
        string="Capacity (L)",
        default=6000.0,
        required=True,
    )
    current_stock = fields.Float(
        string="Current Stock (L)",
    )
    price_per_liter = fields.Float(
        string="Price per Liter",
        default=0.0,
        digits=(16, 2),
    )

    @api.constrains('capacity_liters', 'current_stock')
    def _check_capacity_limits(self):
        for rec in self:
            if rec.capacity_liters and rec.capacity_liters != 6000.0:
                raise ValidationError(_("Tank capacity must be 6000 liters."))
            if rec.current_stock and rec.current_stock < 0:
                raise ValidationError(_("Current stock cannot be negative."))
            if rec.capacity_liters and rec.current_stock and rec.current_stock > rec.capacity_liters:
                raise ValidationError(_("Current stock cannot exceed tank capacity."))
