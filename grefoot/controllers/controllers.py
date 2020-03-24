# -*- coding: utf-8 -*-
from odoo import http
import json
from openerp.http import Response 


class Grefoot(http.Controller):
    @http.route('/grefoot/grefoot/', type='json',website=True,auth='public')
    def index(self, **kw):
        return "I am a live"

    @http.route('/grefoot/api/products/',method=['POST'],auth='public',type="http")
    def list(self, **kw):
        results=http.request.env['product.product'].sudo().search_read([],fields=['name','website_url','product_tmpl_id'])

        headers = {'Content-Type': 'application/json'}
        body={'results':{'code':200,'message':results}}
        return Response(json.dumps(body),status=200,headers=headers)


    @http.route('/grefoot/api/sitesetting/',auth='public',type="http")
    def get_site_settings(self, **kw):
        # results=http.request.env['product.product'].sudo().search_read([],fields=['name','website_url','product_tmpl_id'])

        headers = {'Content-Type': 'application/json'}
        body={'results':{'code':200,'message':{'name':'test'}}}
        return Response(json.dumps(body),status=200,headers=headers)


    @http.route('/shop/update_state', type='json', auth="public", website=True)
    def update_state(self, **kw):
        # results=http.request.env['product.product'].sudo().search_read([],fields=['name','website_url','product_tmpl_id'])

        headers = {'Content-Type': 'application/json'}
        body={'results':{'code':200,'message':{'name':'test'}}}
        return Response(json.dumps(body),status=200,headers=headers)
