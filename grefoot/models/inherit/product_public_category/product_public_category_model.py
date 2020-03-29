# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class product_public_category(models.Model):
    _inherit = 'product.public.category'

    # ----------------------------------------------
    # database
    # ----------------------------------------------

    product_ids = fields.One2many('product.template','public_categ_ids')