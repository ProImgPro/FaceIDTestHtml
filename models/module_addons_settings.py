from odoo import api, fields, models


class ResConfigSettingsAhaMove(models.TransientModel):
    _inherit = 'res.config.settings'

    module_delivery_ahamove = fields.Boolean("AhaMove")




