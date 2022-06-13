from odoo.tests import common, tagged


@tagged('post_install', '-at_install')
class TestMaintenanceEquipmentModel(common.SavepointCase):
    def setUp(self):
        super(TestMaintenanceEquipmentModel, self).setUp()
        self.partner = self.env["res.partner"].create({"name": "Partner A"})
        self.model = self.env["maintenance.equipment.model"].create({"name": "Model A"})

    def test_compute_maintenance_equipment_name_with_serial_number(self):
        equipment = self.env["maintenance.equipment"].create(
            {"partner_id": self.partner.id, "model_id": self.model.id, "serial_no": "#1"}
        )
        self.assertEqual(equipment.name, "Partner A - Model A [#1]")

    def test_compute_maintenance_equipment_name_without_serial_number(self):
        equipment = self.env["maintenance.equipment"].create(
            {"partner_id": self.partner.id, "model_id": self.model.id}
        )
        self.assertEqual(equipment.name, "Partner A - Model A")
