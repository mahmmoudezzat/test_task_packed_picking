# -*- coding: utf-8 -*-
{
    'name': "test_task_packed_picking",

    'summary': """
        Task Module""",

    'description': """
        Task Module
    """,

    'author': "Mahmoud Ezzat",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/picking_menu_views.xml',
        'wizards/stock_wizard_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
