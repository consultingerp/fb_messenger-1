odoo.define('ks_ecommerce_theme.main', function (require) {
    'use strict';
    var ajax = require('web.ajax');

    $(document).ready(function(){

        var ks_head = $("head");
        var $style = $("<style>")
//                    $("#my_cart").remove();
         ajax.jsonRpc("/new_snippets/styles", 'call', {}).then(function (data) {
            _.each(data,function(e){
                $style.append(data.snippets_css);
            });
            ks_head.append($style);
        });
         $("#ex2").slider({});

         // Without JQuery
//                            var slider = new Slider('#ex2', {});

        //Because of this comparision works on homepage
        $('#wrapwrap.homepage main').addClass("oe_structure oe_empty oe_website_sale");
        var pathname = window.location.pathname;
        var parts = pathname.split("/");
        var last_part = parts[parts.length-1];
        //Removing cart page from the payment pages
        if(last_part==="payment" || last_part==="checkout" || last_part==="address" ){
            $("#my_cart_2").remove();
            }

        var owl = $('.ks_multi_image_horizontal');
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

        owl.owlCarousel({
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
                    items: 4,
                },
                1200:{
                    items: 5,
                }
            },
        });

        $(document).on('click', '.ks-vs-img',function(ev){
            var id = $(ev.currentTarget).attr('data-slide-to')

            $(ev.currentTarget.parentElement).siblings().find('.active').removeClass('active')
            $($(ev.currentTarget)).trigger('to.owl.carousel',id).addClass('active')
            $($(ev.currentTarget).parents().find('.ks_main')).find('.owl-stage').trigger('to.owl.carousel',id).addClass('active');
        });


        owl.on('mousewheel', '.owl-stage', function (e) {
            owl.trigger('next.owl');
            e.preventDefault();
        });

        $('.ks_vert_slider').owlCarousel({
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
                    items: 5,
                },
                1200:{
                    items: 5,
                }
            },
        });
    });
});

