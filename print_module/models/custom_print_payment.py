from odoo import fields, models, api


class CustomPayment(models.AbstractModel):
    _name = 'report.print_module.bill_report_container'
    _description = 'Custom Print from'

    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('print_module.bill_report_container')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.account.move,
            'docs': self,
        }
        return docargs
