odoo.define('grefoot.delivery_price', function (require) {
    "use strict"


    var website = require('website.website'),
        base = require('web_editor.base'),
        core = require('web.core'),
        ajax = require('web.ajax'),
        wp = $('#website_partner').data('website-partner'),
        op = $('#order_partner').data('order-partner'),
        state = (op == wp) ? true : false,
        $conf_buttons = $("#checkout_payment_button"),
        $payment = $("#payment_method_buttons"),
        $ship_button = $("#send_same_address"),
        $shipping_form = $("#BillingAddressForm"),
        $shipping_inputs = $shipping_form.find('input[required]'),
        $all_shipping_inputs = $shipping_form.find('input'),
        $billing_form = $("#BillingAddressForm"),
        $card_form = $("#card-form"),
        _t = core._t;
        require('web.dom_ready');

    // var ajax = require('web.ajax'),
    //     website = require('website.website'),
    //     core = require('web.core'),
    //     Widget = require("web.Widget");
    //     require('web.dom_ready');
    function bind_events() {
        // var $carrier = $("#delivery_carrier");
        // $carrier.find("input[name='delivery_type']").each(function () {
        //     $(this).off('click').click(function (ev) {
        //         ajax.jsonRpc('/shop/update_carrier', 'call', {
        //             'carrier_id': Number(ev.currentTarget.value)
        //         }).then(_onCarrierUpdateAnswer);
        //     });
        // })
        // writes the notes on the order
        debugger;

        $("select").css('background-color','red')
        $("select[name='state_id']").on('change', function (ev) {
            var state = $(this).val();
            // ajax.jsonRpc("/shop/check_address/", 'call', {
            //     'state_id': state
            // });
            debugger;
            $shipping_form = $("#BillingAddressForm");
            $billing_form = $("#BillingAddressForm");
            var form_fields = {
                    "name": $shipping_form.find('input[name="name"]').val(),
                    "phone": $shipping_form.find('input[name="phone"]').val(),
                    // "zip": $shipping_form.find('input[name="zip"]').val(),
                    "street": $shipping_form.find('input[name="street"]').val(),
                    "state_id": $shipping_form.find('select[name="state_id"]').val(),
                    "country_id": $shipping_form.find('select[name="country_id"]').val(),
                    "city": $shipping_form.find('input[name="city"]').val(),
                    "csrf_token": $shipping_form.find('input[name="csrf_token"]').val(),
                    "submitted": $shipping_form.find('input[name="submitted"]').val(),
                    // "partner_id": $shipping_form.find('input[name="partner_id"]').val(),
                    "callback": $shipping_form.find('input[name="callback"]').val(),
                    "parent_id": $billing_form.find('input[name="partner_id"]').val()
                }

            $.ajax({
                    type: 'POST',
                    url: '/shop/check_address',
                    data: form_fields,
                    beforeSend: function ( xhr ) {
                        $("#delivery_carrier ul").hide();
                        $('<div class="text-center id="loading_spinner"><span class="fa fa-spinner fa-3x fa-spin"/></div>').insertAfter("#delivery_carrier ul");
                    }
                }).done(function(data) {
                    try {
                        debugger;
                        // var data_obj = $.parseJSON(data);
                        // $billing_form.find('input[name="partner_id"]').val(data_obj.partner_id);
                        $conf_buttons.prop('disabled', false);
                        $("#delivery_carrier ul").show();
                        
                        $("#delivery_carrier ul input[type=radio]:first").each(function(){
                            $(this).attr('checked', true);
                        });

                        $(".fa-spinner").parent().remove();
                    } catch (e) {
                        $conf_buttons.prop('disabled', false);
                        $("#delivery_carrier").replaceWith(data);
                        var cp_id = $("#delivery_carrier").find('#carrier_partner').data('carrier-partner');
                        $billing_form.find('input[name="partner_id"]').val(cp_id);
                        bind_events();
                    }
                });
        });

    }

    window.addEventListener('load', function(){
        setTimeout(()=>{


            bind_events()
        },3000)
      });

})    