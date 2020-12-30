# -*- coding: utf-8 -*-
{
    'name': "Palette Tracking",

    'summary': """
       Palette Tracking Module""",

    'description': """
        Palette Tracking Module
    """,

    'author': "Expert",
    'website': "http://www.yourcompany.com",
    'category': 'Inventory',
    'version': '13.0',
    'depends': ['base', 'sale_management', 'stock', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/palette_tracking.xml',
        'views/partner.xml',
    ],
    'sequence': 1,
    'installable': True,
    'application': False,
    'auto_install': False,

}
