# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class grefoot_product_template(models.Model):
    _inherit = 'product.template'

    # ----------------------------------------------
    # database
    # ----------------------------------------------

    cat_id = fields.Many2one("product.public.category", string="Product Category")
