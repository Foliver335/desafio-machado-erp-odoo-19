from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = "stock.picking"

    fuel_tank_id = fields.Many2one(
        comodel_name="fuel.tank",
        string="Fuel Tank"
    )
    fuel_liters = fields.Float(
        string="Fuel Liters"
    )
    fuel_price_per_liter = fields.Float(
        string="Price per Liter"
    )
    fuel_total_amount = fields.Float(
        string="Total",
        compute="_compute_fuel_total",
        store=True
    )
    fuel_entry_id = fields.Many2one(
        comodel_name="fuel.tank.entry",
        string="Generated Entry",
    )

    @api.depends("fuel_liters", "fuel_price_per_liter")
    def _compute_fuel_total(self):
        for rec in self:
            rec.fuel_total_amount = rec.fuel_liters * rec.fuel_price_per_liter

    @api.constrains("fuel_liters")
    def _check_fuel_liters(self):
        for rec in self:
            if rec.fuel_liters and rec.fuel_liters < 0:
                raise ValidationError(_("Fuel liters cannot be negative."))

    def button_validate(self):
        res = super().button_validate()
        for picking in self:
            if picking.fuel_entry_id:
                continue
            if picking.picking_type_id.code != "incoming":
                continue
            if not picking.fuel_tank_id or not picking.fuel_liters:
                continue
            entry = self.env["fuel.tank.entry"].create({
                "tank_id": picking.fuel_tank_id.id,
                "date": fields.Datetime.now(),
                "liters": picking.fuel_liters,
                "price_per_liter": picking.fuel_price_per_liter or 0.0,
                "source": "purchase",
                "picking_id": picking.id,
                "purchase_id": picking.purchase_id.id if picking.purchase_id else False,
            })
            picking.fuel_entry_id = entry.id
        return res
