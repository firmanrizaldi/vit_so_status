
from odoo import models, fields, api

class SoState(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    state = fields.Selection([
    ('draft', 'Quotation'),
    ('approve1', 'Approve'), #nambah satu approve
    ('sent', 'Quotation Sent'),
    ('sale', 'Sales Order'),
    ('done', 'Locked'),
    ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')