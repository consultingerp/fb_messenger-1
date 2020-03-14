
/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
odoo.define('website_lazy_loading.wk_lazy', function (require) {
    "use strict";
    
    var ajax = require('web.ajax');
	$(document).ready(function(){ 
		$('[data-toggle="popover"]').popover();
		var payments = $(".card-body input[name='pm_id']");
		var codId = false;
		if (payments.length) {
			ajax.jsonRpc("/check/disable", 'call', {})
				.then(function (data) {
					if (data) {
						if (data.isDisable) {
							codId = data.acquirer_id;
							payments.each(function(){
								if ($(this).data('acquirer-id') == codId) {
									$(this).prop('disabled', true);
								}
							});
						}
					}
				}).fail(function (error) {
				});
				payments.on("change", function (event) {
					var pay_button = $('#o_payment_form_pay');
					if ($(this).data('acquirer-id') == codId) {
						$(this).prop('disabled', true);
						pay_button.prop('disabled', true);
					} else {
						pay_button.prop('disabled', false);
					}
				});
		}

	});
})