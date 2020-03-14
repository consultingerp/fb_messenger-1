# -*- coding: utf-8 -*-

from odoo import api, fields, models

class res_company(models.Model):
    _inherit = "res.company"

    whatsapp_number = fields.Char(string='WhatsApp Number')
    button_title = fields.Char(string='WhatsApp Button Title')
    whatsapp_position = fields.Selection([
        ('left', 'Left'),
        ('right', 'Right')
    ], "WhatsApp Position")

