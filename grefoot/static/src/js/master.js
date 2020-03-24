odoo.define('grefoot.delivery_price', function (require) {
    "use strict"


    var website = require('website.website'),
        core = require('web.core')
        require('web.dom_ready');


;
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