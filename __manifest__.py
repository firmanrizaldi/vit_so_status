# -*- coding: utf-8 -*-
{
    'name': "vit_so_state",

    'summary': """
        custom form SO menambahkan field state""",

    'description': """
        custom form SO menambahkan field state
    """,

    'author': "firmanrizaldiyusup@gmai.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/so_status.xml',
    ],
}