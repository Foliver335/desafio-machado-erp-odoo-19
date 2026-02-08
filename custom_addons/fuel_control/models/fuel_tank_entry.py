from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class FuelTankEntry(models.Model):
    _name = "fuel.tank.entry"
    _description = "Fuel Stock Entry"
    _order = "date desc"
    _inherit = ["fuel.control.mixin"]

    tank_id = fields.Many2one(
        comodel_name="fuel.tank",
        string="Fuel Tank",
        required=True
    )
    source = fields.Selection(
        [
            ("manual", "Manual"),
            ("purchase", "Purchase"),
        ],
        string="Source",
        default="manual",
        required=True
    )
    picking_id = fields.Many2one(
        comodel_name="stock.picking",
        string="Receipt",
        
    )
    purchase_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Purchase Order",
        
    )

    @api.constrains("liters")
    def _check_liters(self):
        for rec in self:
            if rec.liters <= 0:
                raise ValidationError(_("Liters must be greater than zero."))

    def _check_capacity(self, tank, liters_delta):
        if not tank:
            return
        new_stock = tank.current_stock + liters_delta
        if tank.capacity_liters and new_stock > tank.capacity_liters:
            raise ValidationError(_("Stock exceeds tank capacity."))

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            self._check_capacity(rec.tank_id, rec.liters)
            rec.tank_id.current_stock = rec.tank_id.current_stock + rec.liters
        return records

    def write(self, vals):
        old_values = {
            rec.id: {
                "tank": rec.tank_id,
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
            new_tank = rec.tank_id
            new_liters = rec.liters
            if old_tank == new_tank and old_liters == new_liters:
                continue
            if old_tank:
                old_tank.current_stock = old_tank.current_stock - old_liters
            self._check_capacity(new_tank, new_liters)
            new_tank.current_stock = new_tank.current_stock + new_liters
        return res

    def unlink(self):
        for rec in self:
            if rec.tank_id:
                rec.tank_id.current_stock = rec.tank_id.current_stock - rec.liters
        return super().unlink()
