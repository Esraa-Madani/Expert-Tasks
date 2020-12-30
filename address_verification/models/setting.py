# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    auth_id = fields.Char(string='Auth Id',config_parameter='address_verification.auth_id')
    auth_token = fields.Char(string='Auth Token',config_parameter='address_verification.auth_token')

    # add api authentication parameter to website configuration
    # use get_values , Set_values method to store value of two new fields

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        auth_id = IrDefault.get('res.config.settings', "auth_id", company_id=self.company_id.id or self.env.user.company_id.id)
        auth_token = IrDefault.get('res.config.settings', "auth_token", company_id=self.company_id.id or self.env.user.company_id.id)
        res.update(
            auth_id=auth_id if auth_id else False,
            auth_token= auth_token if  auth_token else False,
        )
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()

        IrDefault = self.env['ir.default'].sudo()
        IrDefault.set('res.config.settings', "auth_id", self.auth_id,company_id=self.company_id.id)
        IrDefault.set('res.config.settings', "auth_token", self.auth_token, company_id=self.company_id.id)
        return  res


