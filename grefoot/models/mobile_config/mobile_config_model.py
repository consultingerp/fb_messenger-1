# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class grefoot_mobile_config(models.Model):
    _name = 'grefoot.mobile_config'

    facebook_app_id = fields.Char(string="Facebook App ID")

    address = fields.Char(string="Address")

    state = fields.Char(string="State")

    country = fields.Char(string="Country")

    contact_us_email = fields.Char(string="Contact us email")

    latitude = fields.Char(string='Latitude')

    longitude = fields.Char(string='Longitude')

    phone_no = fields.Char(string='Phone Number')

    fcm_android_sender_id = fields.Char(string="fcm android sender id")

    lazzy_loading_effect = fields.Binary(string="Lazzy Loading Effect")

    new_product_duration = fields.Float(string="New Product Duration")

    notification_title = fields.Char(string="Notification Title")

    notification_text = fields.Char(string="Notification Text")

    notification_duration = fields.Float(string="Notification Duration")

    currency_symbol = fields.Char(string="Currency Symbol")

    cart_button = fields.Char(string="Cart Button")

    footer_button = fields.Char(string="Footer Button")

    app_name = fields.Char(string="App Name")

    home_style = fields.Integer(string="Home Style", default=1)

    category_style = fields.Integer(string="Category Style", default=1)

    site_url = fields.Char(string="Site URL")

    intro_page = fields.Char(string="Intro Page")

    my_orders_page = fields.Char(string="My orders page")

    news_page = fields.Char(string="News page")

    wish_list_page = fields.Char(string="Wish List page")

    shipping_address_page = fields.Char(string="Shipping Address page")

    about_us_page = fields.Char(string="About us page")

    contact_us_page = fields.Char(string="Contact us page")

    edit_profile_page = fields.Char(string="Edit Profile page")

    package_name = fields.Char(string="Package Name")

    setting_page = fields.Char(string="Setting page")

    admob = fields.Char(string="Admob")

    ad_unit_id_banner = fields.Char(string="Ad Unit Id Banner")

    ad_unit_id_interstitial = fields.Char(string="Ad Unit Id Interstitial")

    google_analytic_id = fields.Char(string="Google Analytic Id;")

    rate_app = fields.Char(string="Rate App")

    share_app = fields.Char(string="Share App")

    facebook_login = fields.Char(string="Facebook Login")

    google_login = fields.Char(string="Google Login")

    default_notification = fields.Char(string="Default Notification")

    onesignal_app_id = fields.Char(string="OneSignal App Id")

    onesignal_sender_id = fields.Char(string="OneSignal Sender Id")

    ios_admob = fields.Char(string="IOS admob")

    ios_ad_unit_id_banner = fields.Char(string="IOS Ad Unit ID Banner")

    ios_ad_unit_id_interstitial = fields.Char(string="IOS Ad Unit ID Interstitial")

    app_icon_image = fields.Binary(string="App Icon Image")