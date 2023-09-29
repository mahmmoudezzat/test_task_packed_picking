from odoo import models, fields


class TestTaskPackedPicking(models.Model):
    _inherit = 'stock.picking'

    def _create_packed_picking(self, operation_type, stock_move_data, owner=None, location=None, location_dest_id=None,
                               package_name=None, create_lots=False, set_ready=False):
        picking_values = {
            'picking_type_id': operation_type.id,
            'location_id': location.id if location else operation_type.default_location_src_id.id,
            'location_dest_id': location_dest_id.id if location_dest_id else operation_type.default_location_dest_id.id,
            'owner_id': owner.id if owner else False
        }

        picking = self.create(picking_values)
        if package_name:
            picking.write({'name': package_name})
        for move_line in stock_move_data:

            move_values = {
                'product_id': move_line.product_id,
                'reserved_uom_qty': move_line.qty_done,
                'picking_id': picking.id,
                'location_id': location.id,
                'location_dest_id': location_dest_id.id
            }

            move = self.env['stock.move.line'].create(move_values)
            if create_lots:
                if move_line.serial:
                    lot_name = move_line.serial
                    lot_vals = {
                        'name': lot_name,
                        'product_id': move_line.product_id,
                        'company_id': picking.company_id.id,
                        'quant_ids': [
                            (0, 0, {'product_id': move_line.product_id, 'quantity': move_line.qty_done,
                                    'location_id': location.id})],
                    }
                else:
                    lot_vals = {
                        'company_id': picking.company_id.id,
                        'product_id': move_line.product_id,
                        'quant_ids': [
                            (0, 0, {'product_id': move_line.product_id, 'quantity': move_line.qty_done,
                                    'location_id': location.id})],
                    }
                created_lot = self.env['stock.lot'].create(lot_vals)
                move.write({'lot_id': created_lot.id})
                picking.move_line_ids_without_package += move

        if set_ready:
            picking.write({'state': 'assigned'})

        return picking


class StockMoveData(models.Model):
    _name = 'stock.move.data'

    product_id = fields.Integer(string='product')
    qty_done = fields.Float(string='Quantity Done')
    serial = fields.Char('Serial Number')
