odoo.define('website_add_product.website_add_product', function (require) {
"use strict";
var ajax = require('web.ajax');

$(document).ready(function () {
	debugger;
$('.dynamic_add_pro').click(function(){
	debugger;
    ajax.jsonRpc("/shop/cart/update_json", 'call', {
        'product_id': parseInt($(this).attr('product_id'),10),
       
    	'add_qty': 1,})
        .then(function (data) {
        		var $q = $(".my_cart_quantity");
        		var qty = $q.html()
        		if(qty == ''){
        			qty = 0;
        		}
        		$q.html(parseInt(qty)+1).hide().fadeIn(600);
        });
});
});
});