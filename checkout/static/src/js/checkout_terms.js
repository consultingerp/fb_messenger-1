odoo.define('checkout.terms_checkbox', function (require) {
    "use strict";
    const Widget = require("web.Widget");
    const $terms = $('#checkbox_js');
    const termsCheckbox = Widget.extend({
        events: {
            'change input#checkbox_cgv': '_onChange',
        },
        init() {
            this._super.apply(this, arguments);
        },
        _onChange(ev) {
            const $checkbox = $(ev.currentTarget);
            const $pay_button = $('#checkout_payment_button');
            $pay_button.prop('disabled', !$checkbox.prop('checked'));
        }
    });
    require('web.dom_ready');

    if (!$terms.length) {
        return $.Deferred().reject("Dom Does not contain the terms checkbox #checkbox_cgv");
    }

    $terms.each(function () {
        new termsCheckbox().attachTo(this);
    });

    return termsCheckbox;
});
