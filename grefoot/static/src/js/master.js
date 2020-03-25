odoo.define('grefoot.delivery_price', function (require) {
    "use strict"


    var website = require('website.website'),
        core = require('web.core')
        require('web.dom_ready');



    function bind_events_new() {
        $('.ks-scroll-top').hide();
        $('body').scroll(function() {
            
            if ($(this).scrollTop() > 100) {
                $('.ks-scroll-top').fadeIn();
            } else {
                $('.ks-scroll-top').fadeOut();
            }
        
        })}

         bind_events_new()

})    



odoo.define('grefoot.website_add_product_quick', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var Dialog = require('web.Dialog');
    var Widget = require('web.Widget');
    // var Notification = require('web.Notification');




    var timeOutMessageCart;
    function createMessageHighlightCart(){
        // check if already exist then hide and show same one
        if($('#messageHighLightCart').length>0)
        {
            if(timeOutMessageCart)
            {
            clearTimeout(timeOutMessageCart)
            }
            $('#messageHighLightCart').hide()
            $('#messageHighLightCart').fadeIn(100)
            setTimeout(()=>{
                $('#messageHighLightCart').fadeOut(3000)
            },5000)


        }
        else {

       var high='<div id="messageHighLightCart" class="ui-widget ui-corner-all highlightPopUp" style="position:fixed;right:10px;top:50px;z-index:9999999">'
                    +'<p style="margin-bottom: 5px;" >'
                    +'<i class="fa fa-info-circle"></i>'
                    // +'<span class="ui-icon info" style="float:left;margin-right: .3em;"></span>'
                    +'<span> Your product has been added successfully </span>'
                    +'</p>'
                    +'<a href="/shop/cart">'
                    +'<p style=" width: 50%; text-align: center; border: 2px solid white;  margin: 0 auto; border-radius: 50px;">'
                    +'<span>Go to Cart</span>'
                    +'<i class="fa fa-shopping-cart fa-1x" style="float:right;font-size: 1.3em;margin-left:5px;margin-right:5px"></i>'
                    +'</p>'
                    +'</a>'
                    +'</div>'
                    $('body').prepend(high).fadeIn(100);
                     timeOutMessageCart=setTimeout(()=>{
                        $('#messageHighLightCart').fadeOut(3000)
                    },5000)

        }
    }


        $('.ks-add-to-cart-btn').click(function (ev) {
            ev.preventDefault();
            ev.stopPropagation();

            // ServicesMixin.do_notify(("Success"), ("Your product has been added"));
            var product_id = $(this).parent().find('input').val()
            ajax.jsonRpc("/shop/cart/update_json", 'call', {
                'product_id': parseInt(product_id),
                'add_qty': 1,
            })
                .then(function (data) {
                    var $q = $(".my_cart_quantity");
                    var qty = $q.html()
                    if (qty == '') {
                        qty = 0;
                    }
                    $q.html(parseInt(qty) + 1).hide().fadeIn(600);
                   
                    createMessageHighlightCart()

                });
    });
});