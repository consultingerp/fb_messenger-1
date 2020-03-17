# coding: utf-8
# Copyright 2018 Vauxoo
# License OPL-1 (http://opencontent.org/openpub).

{
    'name': 'One Page Checkout',
    'summary': '''
    One Page Checkout
    ''',
    'author': 'Vauxoo',
    'website': 'http://www.vauxoo.com',
    'license': 'LGPL-3',
    'category': 'website',
    'version': '12.0.1.0.4',
    'depends': [
        'website_sale_delivery',
        'base_vat',
    ],
    'test': [
    ],
    'data': [
        'data/image_assets.xml',
        'views/assets.xml',
        'views/checkout.xml',
    ],
    'demo': [
        'demo/res_user_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 99,
    'currency': 'EUR',
    'images': [
        'static/description/main_screen.jpeg'
    ],
}
