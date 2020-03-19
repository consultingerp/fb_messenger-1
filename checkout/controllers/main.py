# coding: utf-8
# Copyright 2018 Vauxoo
# License OPL-1 (http://opencontent.org/openpub).

from __future__ import division
import json
from werkzeug.exceptions import Forbidden
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInh(WebsiteSale):

    @http.route(['/shop/rerender_confirmation'], type='http', auth="public",
                website=True)
    def _get_confirmation_tmpl(self, **kw):
        """Minimal method to re-render the total of the confirmation column.
        """
        order = request.website.sale_get_order()
        order._check_carrier_quotation(force_carrier_id=order.carrier_id)
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection
        values = {
            'website_sale_order': order
        }
        return request.render("checkout.confirm_order", values)

    @http.route(['/shop/check_address'], type='http', auth="public",
                website=True)
    def check_address(self, **kw):
        """Called when the form is complete and valid.
        """
        import pdb;pdb.set_trace()
        partner_obj = request.env['res.partner'].with_context(
            show_address=1).sudo()
        order = request.website.sale_get_order()
        # checking if the user is not here without order and avoid tracebacks
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection
        def_country_id = order.partner_id.country_id
        values, errors = {}, {}
        partner_id = int(kw.get('partner_id', -1))
        # ('new', 'billing') assuming by default public user
        create = 'new'
        ship = 'billing'
        public_partner = request.website.user_id.sudo().partner_id.id
        if partner_id == -1:
            # ('new', 'shipping') creating a new contact
            ship = 'shipping'
        if order.partner_id.id != public_partner and partner_id > 0:
            # ('edit', 'billing') editing a registered main user/contact
            create = 'edit'
        shippings = partner_obj.search([
            ('id', 'child_of', order.partner_id.commercial_partner_id.ids),
            ('id', '=', partner_id)])
        if (partner_id not in shippings.ids and
                partner_id != order.partner_id.id and partner_id > 0):
            return Forbidden()
        if partner_id != order.partner_id.id and partner_id > 0:
            # ('edit', 'shipping') ediging a contact linked to a user
            ship = 'shipping'
        mode = (create, ship)
        values = partner_obj.search([('id', '=', partner_id)])
        pre_values = self.values_preprocess(order, mode, kw)
        errors, error_msg = self.checkout_form_validate(
            mode, kw, pre_values)
        post, errors, error_msg = self.values_postprocess(
            order, mode, pre_values, errors, error_msg)
        errors.update({'error_message': error_msg} if errors else {})
        values = kw if errors else values
        ret_values = {
            'partner_id': partner_id,
            'mode': mode,
            'error': errors,
            'callback': kw.get('callback'),
        }
        if errors:
            return json.dumps(ret_values)
        if ship == 'shipping':
            post['type'] = 'delivery'
            post['parent_id'] = kw.get('parent_id')
        partner_id = self._checkout_form_save(mode, post, kw)
        extra = (lambda order, partner: None, lambda order, partner: None)
        action = {
            'billing': (lambda order, partner: setattr(order,
                        'partner_id', partner),
                        lambda order, partner: order.onchange_partner_id()),
            'shipping': (lambda order, partner: setattr(order,
                         'partner_shipping_id', partner),
                         lambda order, partner: None)
        }
        action.get(mode[1], extra)[0](order, partner_id)
        action.get(mode[1], extra)[1](order, partner_id)
        order.message_partner_ids = [
            (4, partner_id),
            (3, request.website.partner_id.id)]
        country = ('country_id' in values and values['country_id'] != '' and
                   request.env['res.country'].browse(
                       int(values['country_id'])))
        country = country and country.exists() or def_country_id
        partner_id = partner_id if isinstance(
            partner_id, int) else partner_id.id
        carriers = self._get_shop_payment_values(order)
        carriers['partner_id'] = partner_id
        req_rend = request.render("checkout.carriers", carriers)
        return req_rend

    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def payment(self, **post):
        """ Inherited to set delivery method based on rules and available data
        on the order
        """
        order = request.website.sale_get_order()
        c_id = int(post.get('carrier_id', 0))
        order._check_carrier_quotation(force_carrier_id=c_id)
        res = super(WebsiteSaleInh, self).payment(**post)
        for field in self._get_mandatory_billing_fields():
            if not order.partner_id[field]:
                res.qcontext['incomplete_data'] = True
        request.session['sale_last_order_id'] = order.id
        return res

    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):
        """Inherited to avoid old rendering of checkout, the XHR is used
        in JS to be able to call this controller and set the delivery
        address on the order.
        """
        order = request.website.sale_get_order()
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection
        super(WebsiteSaleInh, self).checkout(**post)
        if post.get('xhr'):
            return 'ok'
        return request.redirect('/shop/payment')

    @http.route(['/shop/set_carrier'], type='http', auth="public",
                website=True)
    def set_carrier(self, **post):
        """Mainly used to asynchronously set the carrier to the order.
        """
        order = request.website.sale_get_order()
        carrier_id = int(post.get('carrier_id', 0))
        order._check_carrier_quotation(force_carrier_id=carrier_id)
        return json.dumps({'carrier': carrier_id})

    @http.route(['/shop/render_carriers'], type='http', auth='public',
                website=True)
    def render_carriers(self, **post):
        """Used to render carriers according to the partner set to the order
        as "shipping address"
        """
        partner_id = post.get('partner_id')
        order = request.website.sale_get_order()
        carriers = self._get_shop_payment_values(order)
        carriers['partner_id'] = partner_id
        req_rend = request.render("checkout.carriers", carriers)
        return req_rend

    @http.route(['/shop/editme'], type='http', auth="public", website=True)
    def editme(self, partner_id):
        """Enable the widget to edit a partner/contact
        """
        order = request.website.sale_get_order()
        contact = request.env['res.partner'].sudo().browse(int(partner_id))
        template = 'checkout.edit_contact_form'
        if order.partner_id.id == int(partner_id):
            template = 'checkout.edit_billing_form'
        values = {
            'contact': contact,
            'website_sale_order': order,
        }
        return request.render(template, values)

    @http.route(['/shop/addme'], type='http', auth="public", website=True)
    def addme(self):
        """Enable the widget to add a partner/contact
        """
        return request.render('checkout.add_shipping_address')

    @http.route(['/shop/render_kanban'], type='http', auth="public",
                website=True)
    def render_kanban(self, **post):
        """Renders Kanban after editing/creating a partner/contact
        """
        order = request.website.sale_get_order()
        values = {
            'website_sale_order': order
        }
        return request.render('checkout.shipping_cards', values)

    @http.route(['/shop/render_billing'], type='http', auth="public",
                website=True)
    def render_billing(self, **post):
        """Renders Kanban card of billing partner
        """
        order = request.website.sale_get_order()
        values = {
            'single_partner': order.partner_id
        }
        return request.render('checkout.partner_card', values)

    @http.route(['/shop/address'], type='http',
                methods=['GET', 'POST'], auth="public", website=True)
    def address(self, **kw):
        super(WebsiteSaleInh, self).address()
        return request.redirect('/shop/payment')

    @http.route(['/validators/vat'], type='http', methods=['GET', 'POST'],
                auth="public", website=True)
    def validate_vat(self, **post):
        partner = request.env['res.partner']
        val = partner.public_check_vat(post.get('vat'))
        return json.dumps(val)

    @http.route(['/shop/delivery_instructions'], type='json',
                auth="public", website=True)
    def set_instructions(self, instructions):
        order = request.website.sale_get_order()
        order.write({'note': instructions})

    @http.route()
    def payment_confirmation(self, **post):
        res = super(WebsiteSaleInh, self).payment_confirmation(**post)
        order_id = request.session.get('sale_last_order_id')
        if not order_id:
            return res
        order = request.env['sale.order'].sudo().browse(order_id)
        wiz = request.env['portal.wizard'].sudo().with_context(
            {'active_ids': [order.partner_id.id]}).create({})
        users = wiz.user_ids.filtered(
            lambda u: u.email == order.partner_id.email)
        users.write({'in_portal': True})
        error = users.get_error_messages()
        if error:
            res.qcontext['error'] = error
            return res
        users.action_apply()
        res.qcontext['new_user'] = True
        return res
