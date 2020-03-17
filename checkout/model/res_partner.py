# coding: utf-8
# Copyright 2018 Vauxoo
# License OPL-1 (http://opencontent.org/openpub).

from odoo import models, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def public_check_vat(self, vat):
        """Create a dummy partner and checks the VAT."""
        partner = self.env["res.partner"]
        partner_dummy = partner.new({
            'vat': vat,
            'country_id': self.env.ref('base.mx').id
        })
        res = True
        try:
            partner_dummy.check_vat()
        except ValidationError:
            res = False
        return res
