# © 2022 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MaintenanceEquipmentModel(models.Model):
    _name = "maintenance.equipment.model"
    _description = "Maintenance Equipment Model"

    name = fields.Char(required=True)
    manufacturer_id = fields.Many2one("res.partner")
    active = fields.Boolean(default=True)
