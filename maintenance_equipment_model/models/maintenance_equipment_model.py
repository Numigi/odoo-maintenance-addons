# © Numigi (tm) and all its contributors (https://numigi.com/r/home)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MaintenanceEquipmentModel(models.Model):
    _name = "maintenance.equipment.model"
    _description = "Maintenance Equipment Model"

    name = fields.Char(required=True)
    manufacturer_id = fields.Many2one("res.partner")
    active = fields.Boolean(default=True)
