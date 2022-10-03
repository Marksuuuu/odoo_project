from odoo import fields, models, api


class CustomModule(models.AbstractModel):
    _name = 'report.print_module.vendor_bills_report_container'
    _description = 'Custom Module for Print'

    @api.model
    def _get_report_values(self, docids , data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('print_module.vendor_bills_report_container')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.account.move,
            'docs': self,
        }
        return docargs

    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     docs = self.env['account.move'].browse(docids)
    #     return {
    #           'doc_ids': docids,
    #           'doc_model': 'account.move',
    #           'docs': docs,
    #           'data': data,
    #     }