# -*- coding: utf-8 -*-
from odoo import http
import json
from openerp.http import Response 


class Grefoot(http.Controller):
    @http.route('/grefoot/grefoot/', type='json',website=True,auth='public')
    def index(self, **kw):
        return "I am a live"

    @http.route('/grefoot/api/global/',method=['POST'],auth='public',type='json')
    def record_list(self, **kw):
        model = ""

        data = http.request.params

        if 'model' in data:
            model = data['model']
        else:
            return {'code':404, 'records':records}

        domain = None if 'domain' not in data else data['domain']
        fields = None if 'fields' not in data else data['fields']
        offset = 0 if 'offset' not in data else data['offset']
        limit = None if 'limit' not in data else data['limit']
        order = None if 'order' not in data else data['order']

        headers = {'Content-Type': 'application/json'}

        records = http.request.env[model].sudo().search_read(domain, fields, offset, limit, order)

        if 'product_tmpl_id' in fields:
            for rec in records:
                rec['product_tmpl_id'] = rec['product_tmpl_id'][0]

        return {'code':200,'records':records}


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
