odoo.define('checkout.payment', function (require) {
"use strict";

var ajax = require('web.ajax'),
    website = require('website.website'),
    core = require('web.core'),
    Widget = require("web.Widget");
    require('web.dom_ready');

    var paymentButton = Widget.extend({
      events: {
        'click #checkout_payment_button': 'onClick',
      },
      init: function(parent, options) {
        this._super.apply(this, arguments);
        this.options = _.extend(options || {}, {
        });
      },
      start: function(){
        this.setInitialState();
      },
      onClick: function(ev){
        ev.preventDefault();
        ev.stopPropagation();
        $('#o_payment_form_pay').trigger('click');
      },
      setInitialState: function(){
        $('#o_payment_form_pay').hide();     
      }
    });

    // validate if element exists to bind it
    if (!$("#payment_method_buttons").length) {
      return $.Deferred().reject("Dom Does not contain the pay button #payment_method_buttons");     
    }
    // Bind object to element
    $("#payment_method_buttons").each(function (){
      var $elem = $(this);
      var button = new paymentButton(null, $elem.data());
      button.attachTo($elem);
    });
    return paymentButton;
});
