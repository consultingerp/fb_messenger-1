# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class grefoot_country(models.Model):
    _inherit = 'res.country'

    active = fields.Boolean(string="Active?",default=False)


class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    name = fields.Char(translate=True)
