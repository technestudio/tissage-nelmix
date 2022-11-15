# -*- coding: utf-8 -*-
{
    'name': "Single validation products",

    'summary': """
        The application validates that in a budget or sales order there are no repeated products.""",

    'description': """
        The application establishes a validation in the budgets and sales orders, which shows a message if there is any product repeated between the order lines.
    """,

    'author': "Techne Studio IT & Consulting",
    'website': "https://www.technerp.com/",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    'license': 'GPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        #'security/crear_e_importar_extractos_bancarios.xml',
        #'views/account_bank_statement_restrictions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "images":['static/description/validador_producto_unico.gif'],
}
