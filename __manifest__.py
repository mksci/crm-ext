# -*- coding: utf-8 -*-
{
    'name': "crm_ext",

    'summary': """
        Module extending basic sales form view""",

    'description': """
        Sales > Leads
        
        - On Extra-Info tab adds Contract Info section
        - Create Install tab with assembly details
    """,

    'author': "mksci",
    'website': "http://www.github.com/mksci",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/widoczek.xml',
    ],

}