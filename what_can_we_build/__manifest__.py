# -*- coding: utf-8 -*-
{
    'name': "What Can We Build",
    'summary': "Dynamic What Can We Build Section",
    'description': """
        Module to manage and display what we can build using Odoo.
    """,
    'author': "Your Name",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website'],
    'data': [
        'security/what_can_we_build_security.xml',
        'security/ir.model.access.csv',
        'views/views/what_can_we_build_views.xml',
        'views/templates/what_can_we_build_template.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'what_can_we_build/static/src/css/services_page_styles.css',
        ],
    },

    'application': True,
    'installable': True,
    'auto_install': False,
}
