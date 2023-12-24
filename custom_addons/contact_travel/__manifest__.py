# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'contact_travel',
    'version': '1.0',
    'category': 'ContactTravel',
    'author' : 'TOUABTI Mohamed',
    'sequence': -100,
    'summary': 'Odoo Test Module',
    'description': """
Odoo Test Module.
    """,
    'depends':['contacts'],
    'data':[
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/voyage_view.xml",
        "views/contact_view_inherit.xml",
    ],
    'demo':[],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license':'LGPL-3'
}
