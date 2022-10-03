from odoo import fields, models, api


class CustomPrintPayment(models.AbstractModel):
    _name = 'report.print_module.report_payment_receipt'
    _description = 'Custom Module for Print'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.payment'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.payment',
            'docs': docs,
            'lines': self.some_func(docs),
            'data': data,
        }