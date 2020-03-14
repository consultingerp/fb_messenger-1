# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    You should have received a copy of the License along with this program.
#    If not, see <https://store.webkul.com/license.html/>
#################################################################################
from odoo import http
from odoo.tools.translate import _
from odoo.http import request
import werkzeug
import pprint

from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging
_logger = logging.getLogger("****** COD ******")

class WebsiteSale(WebsiteSale):

    _codfeedbackUrl='/payment/cash_on_delivery/feedback'
    @http.route([_codfeedbackUrl], type='http', auth='public', website=True)
    def cod_payment(self, **post):
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))
        request.env['payment.transaction'].form_feedback(post, 'cash_on_delivery')
        return werkzeug.utils.redirect('/shop/payment/validate')

    @http.route(['/check/disable'], type='json', auth="public", methods=['POST'], website=True)
    def check_disable(self, **post):
        acquirer = request.env['payment.acquirer'].sudo().search(
            [('provider','=','cash_on_delivery')],limit=1
        )
        if acquirer:
            cod_rule = acquirer.cod_rule
            if cod_rule.cod_payment_btn == 'disable':
                if not request.website.is_cod_available(payment_acquirer=acquirer):
                    return {'isDisable':True, 'acquirer_id':acquirer.id}
        return {'isDisable':False, 'acquirer_id':False}

    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        res = super(WebsiteSale, self).product(product, category=category, search=search, **kwargs)

        cod_payment = request.env['payment.acquirer'].sudo().search(
            [('provider','=','cash_on_delivery')],limit=1
        ).cod_rule
        is_cod = request.website.is_cod_available(product)
        if is_cod:
            res.qcontext['cod_availability']  =is_cod
            res.qcontext['cod_payment'] =cod_payment
        return res


    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def payment(self, **post):
        res = super(WebsiteSale, self).payment(**post)
        acquirers = res.qcontext.get('acquirers',[])
        errors =res.qcontext.get('errors',[])
        for acquirer in filter(lambda ac:ac.provider=='cash_on_delivery',acquirers):
            if not request.website.is_cod_available(payment_acquirer=acquirer):
                if acquirer.cod_rule.cod_payment_btn == 'hide':
                    acquirers.remove(acquirer)
                errors.append(
                   ((_('Sorry, We are unable to provide Cash On Delivery.')),acquirer.cod_rule.cod_unavailability_payment_message))
        res.qcontext['acquirers'] =acquirers
        res.qcontext['errors'] =errors
        return res

    @http.route(['/shop/payment/transaction/',
        '/shop/payment/transaction/<int:so_id>',
        '/shop/payment/transaction/<int:so_id>/<string:access_token>'], type='json', auth="public", website=True)
    def payment_transaction(self, acquirer_id, save_token=False, so_id=None, access_token=None, token=None, **kwargs):
        cod_payment = request.env['payment.acquirer'].sudo().search(
            [('provider','=','cash_on_delivery')],limit=1
        )
        if cod_payment:
            cod_rule = cod_payment.cod_rule
            if cod_rule.cod_payment_btn == 'disable':
                if acquirer_id == cod_payment.id:
                    if not request.website.is_cod_available(payment_acquirer=cod_payment):
                        return False
        return super(WebsiteSale, self).payment_transaction(acquirer_id, save_token, so_id, access_token, token, **kwargs)