# -*- coding: utf-8 -*-

{
    'name': 'WhatsApp Live Chat',
    'version': '1.0',
    'category': 'website',
    'sequence': 6,
    'author': 'Webveer',
    'summary': 'This module allows you to add WhatsApp in your Odoo website.',
    'description': "This module allows you to add WhatsApp in your Odoo website.",
    'depends': ['website'],
    'data': [
        'views/template.xml',
        'views/views.xml',
    ],
    'qweb': [

    ],
    'images': [
        'static/description/button.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 15,
    'currency': 'EUR',
}
