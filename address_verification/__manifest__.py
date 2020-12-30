# -*- coding: utf-8 -*-
{
    'name': "Address Verification",

    'summary': """
       Address Verification""",

    'description': """
        Address Verification
    """,

    'author': "Expert",
    'website': "http://www.yourcompany.com",
    'category': 'web',
    'version': '13.0',
    'depends': ['base', 'sale_management', 'website_sale', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/setting.xml',
    ],
    'sequence': 2,
    'installable': True,
    'application': False,
    'auto_install': False,

}
