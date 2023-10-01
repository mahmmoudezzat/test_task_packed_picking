{
    "name": "Test Task Packed Picking",
    'summary': "Task module to add wizard and customization in stock",
    "version": "16.0.1.0.0",
    "website": "https://cetmix.com/",
    "author": "MahmoudEzzat, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    'depends': ['base','stock'],
    'data': [
        'data/stock_move_data.xml',
        'security/ir.model.access.csv',
        'views/picking_menu_views.xml',
        'wizards/stock_wizard_view.xml',

    ],
    'demo': [
        'demo/demo.xml',
    ],
}
