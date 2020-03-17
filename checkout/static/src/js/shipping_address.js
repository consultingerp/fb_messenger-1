odoo.define('checkout.shipping_address', function(require){
    'use strict';

    var checkout = require('checkout.checkout'),
        website = require('website.website'),
        base = require('web_editor.base'),
        core = require('web.core'),
        ajax = require('web.ajax'),
        wp = $('#website_partner').data('website-partner'),
        op = $('#order_partner').data('order-partner'),
        $shipping_check = $('#send_same_address'),
        $shipping_form = $("#shippingAddressForm"),
        $billing_form = $("#BillingAddressForm");

    if ($('.one_kanban .border_primary').length) {
        $shipping_check.parent('label').hide();
    }
    var validatorObj = $shipping_form.validate({
        submitHandler: function() { alert("Submitted!"); },
        rules: {
            phone: {
                digits: true
            },
        }
    });

    $shipping_check.on('click', function(ev) {
        var valid = $billing_form.valid();
        if (!valid) {
            ev.preventDefault();
            return;
        }
        var $to_toggle = $(".all_shippings");
        if (!$(this).is(':checked')) {
            $to_toggle.slideDown();
            $billing_form.slideUp();
            var csrf_token = $billing_form.find('input[name="csrf_token"]').val();
            $.ajax({
                type: 'POST',
                url: '/shop/render_billing',
                data: {
                    csrf_token: csrf_token,
                }
            }).done(function(data){
                $('.js_billing_form').replaceWith(data);
            });
        } else {
            $to_toggle.slideUp();

        }
    });
});
