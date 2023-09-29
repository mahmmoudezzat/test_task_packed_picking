# -*- coding: utf-8 -*-
# from odoo import http


# class TestTaskPackedPicking(http.Controller):
#     @http.route('/test_task_packed_picking/test_task_packed_picking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_task_packed_picking/test_task_packed_picking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_task_packed_picking.listing', {
#             'root': '/test_task_packed_picking/test_task_packed_picking',
#             'objects': http.request.env['test_task_packed_picking.test_task_packed_picking'].search([]),
#         })

#     @http.route('/test_task_packed_picking/test_task_packed_picking/objects/<model("test_task_packed_picking.test_task_packed_picking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_task_packed_picking.object', {
#             'object': obj
#         })
