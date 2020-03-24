odoo.define('ks_theme_kinetik.ProductConfiguratorMixin', function (require) {
    'use strict';

    var ProductConfiguratorMixin = require('sale.ProductConfiguratorMixin');
    var sAnimations = require('website.content.snippets.animation');
    sAnimations.registry.WebsiteSale.include({
        /**
         * Adds the stock checking to the regular _onChangeCombination method
         * @override
         */
        _onChangeCombination: function (){
            var ks_avail = arguments[1];
            arguments[1] = arguments[1].parent();
            this._super.apply(this, arguments);
            arguments[1] = ks_avail;
            ProductConfiguratorMixin._onChangeCombinationStock.apply(this, arguments);
            var per_disc = ((arguments[2].list_price - arguments[2].price)/arguments[2].list_price)*100;
            if (per_disc){
                $('.Percentage-offer').html('( ' + Math.floor(per_disc) + '% OFF)');
            }
            else{
                $('.Percentage-offer').html("")
            }
            var ks_img_vrnt = $('.ks_thumb').find('.ks_img_vrnt');
            if (ks_img_vrnt.length){
                $('.ks_thumb').find('.owl-stage').trigger('to.owl.carousel', ks_img_vrnt.attr('data-slide-to'));
                $('.ks_main').find('.owl-stage').trigger('to.owl.carousel', ks_img_vrnt.attr('data-slide-to'));
            }

            var seconds = arguments[2].seconds;
            if(seconds){
           $('.ks_product_timer_title').removeClass("d-none");
             $('.clock').removeClass("d-none");
             $('.ks_timer_box').removeClass("d-none");
             var clock = $('.clock').FlipClock(seconds, {
                clockFace: 'DailyCounter',
                            countdown: true,
                });
            }
            else{
                $('.clock').addClass("d-none");
                $('.ks_timer_box').addClass('d-none');
                $('.ks_product_timer_title').addClass("d-none");
            }

        },
    });

    return ProductConfiguratorMixin;
});

odoo.define('ks_theme_kinetik.website_sale', function (require) {
'use strict';

    var website_sale = require('website_sale.website_sale');
    var sAnimations = require('website.content.snippets.animation');

    sAnimations.registry.WebsiteSale.include({
        _updateProductImage: function () {
            this._super.apply(this, arguments);
            var product_length= $('.ks_multi_image_horizontal .ks_active_variant_image').length
            var ks_loop=true;
            if(product_length){
                if (product_length < 5){
                    ks_loop=false;
                }
            }
                else{
                product_length = $('.ks_vert_slider .ks_active_variant_image').length
                if (product_length < 5){
                    ks_loop=false;
                }
            }

            $('.ks_main').on('click', '.owl-next, .owl-prev', function (ev) {
                if($(ev.currentTarget).parents().eq(1).find('.ks_img_vrnt').length){
                    if($(ev.currentTarget).parents().eq(1).find('.center').children().attr('Class').includes('ks_img_vrnt')){
                        $($(ev.currentTarget).parents().find('.ks_thumb')).find('.owl-stage').trigger('to.owl.carousel', 0);
                    }
                    else{
                        var id = $(ev.currentTarget).parents().eq(1).find('.center').children().attr('data-oe-id');
                        $($(ev.currentTarget).parents().find('.ks_thumb')).find('.owl-stage').trigger('to.owl.carousel', id);
                    }
                }
                else{
                    var id = $(ev.currentTarget).parents().eq(1).find('.center').children().attr('data-oe-id');
                    $($(ev.currentTarget).parents().find('.ks_thumb')).find('.owl-stage').trigger('to.owl.carousel', id);
                }
            });


            $('.ks_thumb').on('click', '.owl-next, .owl-prev', function (ev2) {
                $($($(ev2.currentTarget).parent().siblings()[0]).find('.owl-item.active').children()).removeClass('active').addClass('ks-vs-img ks_active_variant_image')
                $($($(ev2.currentTarget).parent().siblings()[0]).find('.owl-item.active.center').children()).addClass('active')
            });

            $('.ks_main').owlCarousel({
                loop:ks_loop,
                nav:true,
                dots:false,
                items:1,
                center:true,
                video:true,
                margin:5,
                navText:['<i class="fa fa fa-angle-left"></i>','<i class="fa fa fa-angle-right"></i>'],
            });

            $('.ks_thumb').owlCarousel({
                loop:ks_loop,
                nav:true,
                center:true,
                dots:false,
                items : 5,
                margin: 5,
                navText:['<i class="fa fa fa-angle-left"></i>','<i class="fa fa fa-angle-right"></i>'],
                responsiveClass: true,
                responsive:{
                    0:{
                        items: 3,
                    },
                    420: {
                        items: 4,
                    },
                    767: {
                        items: 3,
                    },
                    1200:{
                        items: 5,
                    }
                },
            });
            $('.ks_thumb').on('mousewheel', '.owl-stage', function (e) {
                $('.ks_thumb').trigger('next.owl');
                e.preventDefault();
            });
        }
    })
})