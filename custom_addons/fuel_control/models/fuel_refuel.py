from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class FuelRefuel(models.Model):
    _name = "fuel.refuel"
    _description = "Refuel"
    _order = "date desc"
    _inherit = ["fuel.control.mixin"]
    _rec_name = "vehicle_id"

    vehicle_id = fields.Many2one(
        comodel_name="fleet.vehicle",
        string="Vehicle/Plate",
        required=True
    )

    odometer = fields.Float(
        string="Odometer",
        help="Measures the distance traveled in kilometers or Miles"
    )

    hour_meter = fields.Float(
        string="Hour Meter",
        help="Measure the operating time of the engine or equipment (hours)."
    )

    driver_id = fields.Many2one(
        related="vehicle_id.driver_id",
        store=True,
    )
    
    fuel_tank_id = fields.Many2one(
        comodel_name="fuel.tank",
        string="Fuel Tank",
        required=True
    )

    @api.onchange("fuel_tank_id")
    def _onchange_fuel_tank_id(self):
        for rec in self:
            if rec.fuel_tank_id and not rec.price_per_liter:
                rec.price_per_liter = rec.fuel_tank_id.price_per_liter

    @api.constrains("liters")
    def _check_liters(self):
        for rec in self:
            if rec.liters <= 0:
                raise ValidationError(_("Liters must be greater than zero."))
            
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if not rec.price_per_liter and rec.fuel_tank_id:
                rec.price_per_liter = rec.fuel_tank_id.price_per_liter
            if rec.fuel_tank_id.current_stock < rec.liters:
                raise ValidationError(_("Insufficient tank stock."))
            rec.fuel_tank_id.current_stock = rec.fuel_tank_id.current_stock - rec.liters

        return records

    def write(self, vals):
        old_values = {
            rec.id: {
                "tank": rec.fuel_tank_id,
                "liters": rec.liters,
            } for rec in self
        }
        res = super().write(vals)
        for rec in self:
            old = old_values.get(rec.id)
            if not old:
                continue
            old_tank = old["tank"]
            old_liters = old["liters"]
            new_tank = rec.fuel_tank_id
            new_liters = rec.liters
            if old_tank == new_tank and old_liters == new_liters:
                continue
            if old_tank:
                old_tank.current_stock = old_tank.current_stock + old_liters
            if new_tank.current_stock < new_liters:
                raise ValidationError(_("Insufficient tank stock."))
            new_tank.current_stock = new_tank.current_stock - new_liters
        return res

    def unlink(self):
        for rec in self:
            if rec.fuel_tank_id:
                rec.fuel_tank_id.current_stock = rec.fuel_tank_id.current_stock + rec.liters
        return super().unlink()
