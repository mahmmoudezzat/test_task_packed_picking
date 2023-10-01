from odoo import models, fields


class PackProductsWizard(models.TransientModel):
    _name = 'pack.products.wizard'
    _description = 'Pack Products Wizard'

    operation_type_id = fields.Many2one('stock.picking.type', string='Operation Type', required=True)
    stock_move_data = fields.Many2many('stock.move.data', string='Stock Move Data')
    location_id = fields.Many2one('stock.location', string='Source Location')
    location_dest_id = fields.Many2one('stock.location', string='Destination Location')
    owner_id = fields.Many2one('res.partner', string='Owner')
    package_name = fields.Char(string='Package Name')
    create_lots = fields.Boolean(string='Create Lots')
    set_ready = fields.Boolean(string='Set Ready')

    def pack_products(self):
        stock_picking = self.env['stock.picking']
        stock_picking._create_packed_picking(
            self.operation_type_id,
            self.stock_move_data,
            owner=self.owner_id,
            location=self.location_id,
            location_dest_id=self.location_dest_id,
            package_name=self.package_name,
            create_lots=self.create_lots,
            set_ready=self.set_ready,
        )
