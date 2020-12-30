# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class PaletteTracking(models.Model):
    _name = 'palette.tracking'
    _description = 'Palette Tracking'
    _inherit = ['mail.thread']
    _rec_name = 'picking_id'

    picking_id = fields.Many2one('stock.picking', string='Picking', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    license_plate = fields.Char("License")
    picking_partner_id = fields.Many2one('res.partner', string='Picking Partner', related="picking_id.partner_id", store=True)
    picking_date_done = fields.Datetime("Picking Date Done", related="picking_id.date_done", store=True)
    palette_count_plus = fields.Integer(string='Palette Count+')
    palette_count_minus = fields.Integer(string='Palette Count-')
    balance = fields.Integer(string='Balance', compute='_compute_balance')

    @api.depends('palette_count_plus', 'palette_count_minus')
    def _compute_balance(self):
        for rec in self:
            rec.balance = rec.palette_count_plus - rec.palette_count_minus


