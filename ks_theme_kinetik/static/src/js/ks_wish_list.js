odoo.define('ks_theme_website_wishlist', function (require) {
    'use strict'
    var ks_WishList = require('website_sale_wishlist.wishlist');
    var sAnimations = require('website.content.snippets.animation');
    var wSaleUtils = require('website_sale.utils');
    var core = require('web.core');
    var Qweb = core.qweb;
    var ajax = require('web.ajax');

    sAnimations.registry.ProductWishlist.include({
     template: 'ks_shop_old',
     xmlDependencies: ['/ks_theme_kinetik/static/src/xml/ks_main_slider.xml'],
    _addOrMoveWish: function (e) {
    var $def = this._super(e);
        $('#my_cart_2').removeClass('d-none');
        return $def
    },
    _updateWishlistView: function () {
        $('#my_wish').show();
        $('.my_wish_quantity').text(this.wishlistProductIDs.length);
    },
    _addNewProducts: function ($el) {
        var self = this;
        var productID = $el.data('product-product-id');
        if ($el.hasClass('o_add_wishlist_dyn')) {
            productID = $el.parent().find('.product_id').val();
            if (!productID) { // case List View Variants
                productID = $el.parent().find('input:checked').first().val();
            }
            productID = parseInt(productID, 10);
        }
        var $form = $el.closest('form');
        var templateId = $form.find('.product_template_id').val();
        // when adding from /shop instead of the product page, need another selector
        if (!templateId) {
            templateId = $el.data('product-template-id');
        }
        $el.prop("disabled", true).addClass('disabled');
        var productReady = this.selectOrCreateProduct(
            $el.closest('form'),
            productID,
            templateId,
            false
        );

        productReady.done(function (productId) {
            productId = parseInt(productId, 10);

            if (productId && !_.contains(self.wishlistProductIDs, productId)) {
                return self._rpc({
                    route: '/shop/wishlist/add',
                    params: {
                        product_id: productId,
                    },
                }).then(function () {
                    self.wishlistProductIDs.push(productId);
                    self._updateWishlistView();
                    if ($el.parents().eq(2).attr('Class').includes("ks_shop_slider")){
                        var product_id=$el.parents().eq(2).parents('.oe_product_cart').find('.ks_product_template_id').val();
                        var href = $($el.parents().eq(2).find('.oe_product_image').children()[0]).attr('href');
                        var Html = $(Qweb.render('ks_shop_new', {"product_id": product_id,"href" : href,}));
                        $el.parents().eq(2).find('.ks_prod_img').replaceWith(Html[0]);
                        wSaleUtils.animateClone($('#my_wish'), $el.closest('form'), 25, 40);
                        ajax.jsonRpc("/shop/product/slider", 'call', {'product_id':product_id,'href': href}).then(function (data){
                            $el.parents().eq(2).find('.ks_shop_product').parents().eq(0).replaceWith(data);
                            $('.ks_main_for_hover_slider').owlCarousel({
                            dots :true,
                            loop:true,
                            items:1,
                            slideTransition: 'linear',
                            autoplayTimeout: 0,
                            margin:8,
                        });
                        });
                    }
                    else{
                         wSaleUtils.animateClone($('#my_wish'), $el.closest('form'), 25, 40);
                    }
                }).fail(function () {
                    $el.prop("disabled", false).removeClass('disabled');
                });
            }
        }).fail(function () {
            $el.prop("disabled", false).removeClass('disabled');
        });
    },
    });
});

odoo.define('ks_theme_website_compare', function (require) {
    'use strict'
    var ks_Compare = require('website_sale_comparison.comparison');
    var sAnimations = require('website.content.snippets.animation');
    var wSaleUtils = require('website_sale.utils');
    var core = require('web.core');
    var Qweb = core.qweb;
    var ajax = require('web.ajax');
    var el;

    sAnimations.registry.ProductComparison.include({

        template: 'ks_shop_old',
        xmlDependencies: ['/ks_theme_kinetik/static/src/xml/ks_main_slider.xml'],

        _onClickAddCompare: function (ev) {
             if($(ev.currentTarget).parents().eq(3).attr('Class').includes("ks_shop_slider")){
                el = ev.currentTarget;
                var product_id=$(el).parents('.oe_product_cart').find('.ks_product_template_id').val();
                var href = $($(el).parents('.oe_product_cart').find('.oe_product_image').children()[0]).attr('href')
                var Html = $(Qweb.render('ks_shop_new', {"product_id": product_id,"href" : href,}));
                $(el).parents('.oe_product_cart').find('.ks_prod_img').replaceWith(Html[0]);
                this.productComparison.handleCompareAddition($(ev.currentTarget));
                ajax.jsonRpc("/shop/product/slider", 'call', {'product_id':product_id,'href': href}).then(function (data){
                    $(el).parents().eq(3).find('.ks_shop_product').parents().eq(0).replaceWith(data);
                    $('.ks_main_for_hover_slider').owlCarousel({
                        dots :true,
                        loop:true,
                        items:1,
                        slideTransition: 'linear',
                        autoplayTimeout: 0,
                        margin:8,
                    });
                });
             }
             else{
                this.productComparison.handleCompareAddition($(ev.currentTarget));
             }

        },
    })
})
