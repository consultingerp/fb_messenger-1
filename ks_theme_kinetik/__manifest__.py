{
    'name': "Theme Kinetik",

    'summary': """
        Latest, Fully-responsive, Best Odoo theme suitable for e-commerce businesses with 110+ snippets. Extremely customizable, Modern, and supports all type of e-commerce business.""",

    'description': """
        ecommerce theme,
        best ecommerce theme,
        frontend theme,
        odoo theme,
        spa theme,
        beauty theme,
        fitness theme,
        corporate theme,
        business theme,
        enterprise theme,
        community theme,
        community,
        enterprise,  
        best enterprise theme,
        best community theme,
        best odoo theme,
        best odoo themes,
        top odoo theme,
        top frontend odoo theme,
        best frontend odoo theme,
        clarico,
        alan,
        number 1 odoo theme,
        number 1 theme,
        beautiful odoo theme,
        stunning odoo theme,
        Ksolves,
        Ksolves India Private Limited,
        Ksolves India Pvt. Ltd.
        Ksolves India Private Limited odoo apps,
        Ksolves India Pvt. Ltd. odoo apps,
        Ksolves odoo apps,
        Ksolves apps,
        Ksolves odoo,
        Ksolves odoo themes,
        Ksolves themes,
        Ksolves theme,
        Ksolves odoo app, 
        odoo apps,
        Cart Icon Pop Up Themes,
        Outstanding Landing pages Themes,
        GYM Themes,
        Multi Template Themes,
        Customized Themes,
        Customized Odoo Themes,
        Main Image Slider Themes,
        Featured Snippet Themes,
        Brand Snippet Themes,
        Advanced Search Themes,
        Alternative Product Slider Themes,
        Accessory Slider Themes,
        Dynamic Snippet Themes,
        Dynamic Themes,
        Best frontend themes,
        Odoo Corporate Themes,
        Odoo Enterprise Themes,
        Best Odoo ecommerce themes
        Odoo Themes,
        Themes,
        Themes For Odoo,
        Food Store Themes,
        Store Themes,
        Attractive Theme For ecommerce,
        Fitness Themes,
        Jewellery Store Themes,
        Jewellery Themes,
        Jewelry Themes,
        Health Store Themes,
        Health Store,
        Multi Tab Slider Themes,
        Current View Snippets,
        Snippets Themes,
        Breadcrumb Themes,
        Product Per Page Themes,
        Grid View,
        Product Infinity Loader,
        Auto Product Load Themes,
        Automatic Product Load,
        Autoload Themes,
        Furniture Themes,
        Furniture Store Themes,
        Odoo Business Themes,
        Best Blog Snippets,
        Blog Snippets Themes,
        Multiple Product Grid,
        Mega Menu Themes,
        offer snippet Themes,
        Timer snippet Themes,
        Custom Snippet Builder Theme,
        Recently Viewed Snippet Themes,
        Cart Icon Pop-Over Themes,
        Icon Pop Up Themes,
    """,

    'author': "Ksolves India Pvt. Ltd.",
    'website': "https://www.ksolves.com",
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': '170.0',
    'category': 'Theme/Ecommerce',
    'support': 'sales@ksolves.com',
    'version': '1.8.3',
    'live_test_url': 'https://demokinetik.kappso.com',
    'depends': ['ks_theme_base', 'website_sale_wishlist', 'website_sale_comparison',
                'website_sale_stock', 'website_rating','website_crm'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ks_assets.xml',
        'views/ks_header_layouts.xml',
        'views/ks_theme_customization_modal.xml',
        'views/ks_user_custom_snippet.xml',
        'views/ks_shop_view.xml',
        'views/ks_video_snippet.xml',
        # Snippets call
        'views/ks_snippets.xml',
        # Cart
        'views/ks_cart.xml',

        # fonts
        'views/ks_fonts.xml',
        # buttons
        'views/ks_buttons_style.xml',

        # Snippets
        'views/ks_home_main_carousal.xml',
        'views/ks_contactus.xml',
        'views/ks_brand_snippet.xml',
        'views/ks_featured_snippet.xml',
        'views/ks_Blogs.xml',
        'views/ks_blog_page.xml',
        'views/ks_all_static_snippets.xml',
        'views/ks_new_snippets.xml',
        'views/ks_product_detail.xml',
        'views/ks_product_grid_template.xml',
        'views/ks_my_account.xml',
        'views/ks_inherited_website_menu.xml',
        'views/ks_product_multi_slider.xml',
        'views/ks_mega_menu.xml',
        'views/ks_trendy_style_view.xml',
        'views/ks_offer_snippet.xml',
        'views/product_details_quick_view.xml',
        'views/ks_all_static_snippets_animation.xml',
        'views/ks_muti_tab_slider.xml',
        'views/ks_mutitab_backend_view.xml',
        'views/ks_inherited_slider_form.xml',
        'views/ks_recently_viewed_products.xml',
        'views/ks_update_all_slider_view.xml',
        'views/ks_breadcumb_image.xml',
        'views/ks_deal_of_the_day_new.xml',
        'views/ks_blog_detail.xml',

        # landing pages
        'views/ks_theme_beauty.xml',
        'views/ks_inherited_blogs.xml',
        'views/ks_website_contact_us_form.xml',
        # Footer layout
        'views/ks_footer_layout.xml',
        'views/ks_footer_view.xml',
        'data/ks_footer_data.xml',
        'data/ks_demo_data.xml',
    ],

    'qweb': [
        'static/src/xml/ks_offer_timer.xml',
        'static/src/xml/ks_featured_snippet_inner.xml',
        'static/src/xml/ks_new_snippet.xml',
        'static/src/xml/ks_dynamic_blogs.xml',
        'static/src/xml/ks_products_list.xml',
        'static/src/xml/ks_footer_layout.xml',
        'static/src/xml/ks_main_slider.xml',
        'static/src/xml/ks_product_slider_multi.xml',
        'static/src/xml/ks_product_grid_multi.xml',
        'static/src/xml/ks_blogs_slider.xml',
        'static/src/xml/ks_product_grid_snippet.xml',
        'static/src/xml/ks_trendy_style_qweb.xml',
        'static/src/xml/ks_trendy_style_silder_qweb.xml',
        'static/src/xml/ks_blogs_slider_multi.xml',
        'static/src/xml/ks_trendy_style_slider_qweb_multi.xml',
        'static/src/xml/ks_product_grid.xml',
        'static/src/xml/modal.xml',
        'static/src/xml/ks_product_offer.xml',
        'static/src/xml/ks_multitab_slider_inside.xml',
        'static/src/xml/ks_attach.xml',
        'static/src/xml/ks_brand.xml',
        'static/src/xml/ks_deal_of_the_day.xml',
        'static/src/xml/pos_web_editor_backend.xml',
    ],
    'images': [
            'static/description/banner.jpg',
            'static/description/list_screenshot.gif',
    ],
    'demo': [
        'demo/ks_theme_demo_data.xml',
    ],

    "application": True,
    "installable": True,

}
