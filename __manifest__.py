{
    "name": "AhaMove Express",
    "summary": """Integration App In Odoo With Delivery In Company AhaMove"
               Developed by Magenest JSC """,
    "version": "13.0.1.0.0",
    "category": "Extra Tools",
    "website": "http://www.magenest.com",
    "author": "Magenest",
    "license": "OPL-1",
    "data": [
        "views/config_setting_ahamove.xml",
        "views/config_delivery_carrier_form.xml",
    ],
    "depends": [
        "web",
        'hr',
        'delivery',
    ],
    'images': ['static/images/icon.png'],
    "installable": True,
    'images': ['static/description/images/ahamove.png'],
}
