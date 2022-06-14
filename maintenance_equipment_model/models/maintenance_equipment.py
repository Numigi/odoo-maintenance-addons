# © 2022 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result

    model_id = fields.Many2one(
        "maintenance.equipment.model",
        domain="[('manufacturer_id','=?',partner_id)]",
        required=True
    )
    name = fields.Char(compute="_compute_name", store=True, required=False)
    partner_id = fields.Many2one(required=True)

    @api.depends("partner_id", "model_id", "serial_no")
    def _compute_name(self):
        for rec in self:
            if rec.serial_no:
                rec.name = "{} - {} [{}]".format(
                    rec.partner_id.name, rec.model_id.name, rec.serial_no
                )
            else:
                rec.name = "{} - {}".format(rec.partner_id.name, rec.model_id.name)

    @api.onchange("model_id")
    def _onchange_model_id(self):
        if self.model_id.manufacturer_id:
            self.partner_id = self.model_id.manufacturer_id
