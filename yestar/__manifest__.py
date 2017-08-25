# -*- coding: utf-8 -*-
{
    "name": "Falinwa Dealer Car",
    "version": "1.0",
    "author": "Kiki Falinwa Indonesia",
    "description": """
        Module Car Dealer Indonesia.
    """,
    "depends": ["base", 'sale'],
    "init_xml": [],
    "data": [
        'views/yst_product.xml',
        'views/yst_doc_car_sale.xml',
        'views/yst_inherit.xml',
        'security/ir.model.access.csv',  
    ],
    "active": False,
    "application": False,
    "installable": True,
}
