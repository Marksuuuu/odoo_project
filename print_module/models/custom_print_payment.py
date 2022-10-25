from odoo import fields, models, api


class CustomPayment(models.AbstractModel):
    _name = 'report.print_module.report_payment_receipt'
    _description = 'Custom Print from'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('print_module.report_payment_receipt')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.account.payment,
            'docs': self,
        }
        return docargs
