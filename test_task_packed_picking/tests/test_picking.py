from odoo.tests.common import TransactionCase


class TestPackedPicking(TransactionCase):

    def _pack_products_Wizard_data(self):
        return {'package_name': "test",
                'create_lots': False,
                'set_ready': True}

    def test_create_packed_picking(self):
        print("hellow")
        picking_Wizard_data = self._pack_products_Wizard_data()

        picking_values = {
            "name": picking_Wizard_data['package_name'],
            "location_id": self.stock_location.id,
            "location_dest_id": self.customer_location.id,
            "picking_type_id": self.env.ref("stock.picking_type_in").id,
            "owner_id": self.company_partner.id,
        }
        # --log - level = test
        picking_stock_pack = self.env['stock.picking'].create(picking_values)
        stock_move_data = self.env.ref("test_task_packed_picking.stock_move_date")

        move_values = {
            "product_id": self.product.id,
            'reserved_uom_qty': stock_move_data.qty_done,
            'picking_id': picking_stock_pack.id,
            "location_id": self.stock_location.id,
            "location_dest_id": self.customer_location.id,
        }
        move = self.env['stock.move.line'].create(move_values)
        lot_id = self.env['stock.lot'].create({
            'name': stock_move_data.serial,
            'product_id': self.product.id,
            'company_id': self.env.company.id,
        })
        self.env['stock.quant']._update_available_quantity(self.product, self.stock_location, stock_move_data.qty_done,
                                                           lot_id=lot_id)

        move.write({'lot_id': lot_id.id})
        if picking_Wizard_data['set_ready']:
            picking_stock_pack.write({'state': 'assigned'})
        self.assertEqual(picking_stock_pack.state, 'assigned')

    def setUp(self):
        super(TestPackedPicking, self).setUp()
        self.product = self.env["product.product"].search([], limit=1)
        self.company_partner = self.env.ref("base.main_partner")
        self.stock_location = self.env.ref("stock.stock_location_stock")
        self.customer_location = self.env.ref("stock.stock_location_customers")
