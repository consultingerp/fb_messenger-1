
from odoo import api, fields, models

class CodAccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def action_invoice_paid(self):
        res = super(CodAccountInvoice,self).action_invoice_paid()
        if self and self.state == "paid":
            orders = self.env["sale.order"].search([("invoice_status", "=","invoiced"),("partner_id","=",self.partner_id.id)]).filtered(lambda order : self.id in order.invoice_ids.ids)
            for order in orders:
                if all([inv.state == "paid" for inv in order.invoice_ids]):
                    payment_transections = order.transaction_ids.filtered(lambda txn : txn.state == "pending" and txn.provider == "cash_on_delivery" )
                    if payment_transections:
                        payment_transections[0].state = "done"
        return res
