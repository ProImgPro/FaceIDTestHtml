{
    "name": "AhaMove Express",
    "summary": "Integration App In Odoo With Delivery In Company AhaMove",
    "version": "12.0.1.0.0",
    "category": "web",
    "author": "Dev Manegest",
    "license": "LGPL-3",
    "data": [
        "views/config_setting_ahamove.xml",
        "views/config_delivery_carrier_form.xml",
    ],
    "depends": [
        "web",
        'hr',
        'delivery',
    ],
    "installable": True,
}
