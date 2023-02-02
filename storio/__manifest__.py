# -*- coding: utf-8 -*-
{
    'name': "Storio",

    'summary': """
        App to manage a storage""",

    'description': """
        App with a system with admins and users to manage a storage being able to book packs
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'views/security.xml',
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/items.xml',
        'views/bookings.xml',
        'views/model_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}