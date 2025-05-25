# -*- coding: utf-8 -*-
{
    'name': 'myFirstModule',
    'version': '1.0',
    'summary': 'Module Summary',
    'sequence': -100,
    'description': """Module Description""",
    'category': 'Category',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/template.xml',
        'views/lowView.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
