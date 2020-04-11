# -*- coding: utf-8 -*-
from odoo import http
import json
import openerp.addons.web.controllers.main as main
from openerp.http import Response , request

class Extension(main.Session):

    @http.route('/web/session/authenticate', type='json', auth="none",csrf=False,website=False)
    def authenticate(self, db, login, password, base_location=None):
        uid=request.session.authenticate(db,login.lower(),password)
        response_arr = []
        if uid==False:
             response_arr.append({"code": 406, "message":'user not registered'})
             return response_arr
        partner=request.env['res.partner'].sudo().search([('user_ids','=',uid)])
        if bool(partner) == False :
           response_arr.append({"code": 404, "message": 'partner not exist'})
           return response_arr
        else:
            data = {
            "phone": partner.phone,
            "id": partner.id,
            "name": partner.name,
            "image": partner.image,
            "birthdate": "",
            "lat": "",
            "long": "",
            "mobile": partner.mobile,
            "lang": partner.lang,
            "country_id": partner.country_id.id,
            "state_id": partner.state_id.id,
            "email": partner.email,
            "uid": uid,
            "active": partner.active,
            "property_product_pricelist": partner.property_product_pricelist,
            "login": login,
            "gender": "",
            "debit": partner.debit,
            "credit": partner.credit,
            "password": password
            }
            response_arr.append({"code": 200, "data":data})
            return response_arr

class Grefoot(http.Controller):
    @http.route('/grefoot/grefoot/', type='json',website=True,auth='public')
    def index(self, **kw):
        return "I am a live"

    @http.route('/grefoot/api/signup/', type='json',method=['POST'],auth='public')
    def register(self, **kw):
        data = http.request.params

        is_identical = False
        
        if 'password' in data and 'confirm_password' in data:
            if data['password'] == data['confirm_password']:
                is_identical = True

        if is_identical:
            if 'customers_firstname' in data and 'email' in data:
                user = request.env['res.users'].sudo().create({
                    'password': data['password'],
                    'name': data['customers_firstname'],
                    'login': data['email'],
                    'active': True
                    })
            else:
                return {'code':404, 'message':'missing username or email'}
        else:
            return {'code':404, 'message':'passwords not identical'}
        
        if user:
            partner = request.env['res.partner'].sudo().search([('user_ids','=',user.id)])
            if partner:
                partner.phone = data['customers_telephone']

                data = {
                    "phone": partner.phone,
                    "id": partner.id,
                    "name": partner.name,
                    "image": partner.image,
                    "birthdate": "",
                    "lat": "",
                    "long": "",
                    "street": partner.street,
                    "parent_id": partner.parent_id,
                    "mobile": partner.mobile,
                    "lang": partner.lang,
                    "country_id": partner.country_id.id,
                    "state_id": partner.state_id.id,
                    "email": partner.email,
                    "uid": user.id,
                    "active": partner.active,
                    "property_product_pricelist": partner.property_product_pricelist,
                    "login": data['email'],
                    "gender": "",
                    "debit": partner.debit,
                    "credit": partner.credit,
                    "type": partner.type,
                    "password": data['password']
                }
            else:
                return{'code': 200, 'message': 'partner not found', 'records': {}}

        return {'code': 200, 'message': 'user registored successfully', 'records':data}

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
