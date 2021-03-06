# © 2022 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Maintenance Equipment Model",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://bit.ly/numigi-com",
    "license": "LGPL-3",
    "category": "Maintenance",
    "summary": "Add maintenance equipment model and compute equipment's name",
    "depends": [
        "base_maintenance_group",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/maintenance_equipment.xml",
        "views/maintenance_equipment_model.xml",
    ],
    "installable": True,
}
