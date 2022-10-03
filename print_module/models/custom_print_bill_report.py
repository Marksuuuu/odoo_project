from odoo import fields, models, api


class CustomModuleBills(models.AbstractModel):
    _name = 'report.print_module.bill_report_container'
    _description = 'Custom Module for Print'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'lines': self.some_func(docs),
            'data': data,
        }