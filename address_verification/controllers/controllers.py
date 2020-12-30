# -*- coding: utf-8 -*-
from odoo import fields, http, _
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
from odoo.addons.website_sale.controllers.main import WebsiteSale
from smartystreets import Client


class CheckoutWebsite(WebsiteSale):
    # inherit class amd overide address method

    def checkout_form_validate(self, mode, all_form_values, data):
        """ To override Shipping Address submit button controller, inherit from its class
         # mode: tuple ('new|edit', 'billing|shipping')
        # all_form_values: all values before preprocess
        # data: values after preprocess
            """
        res = super(CheckoutWebsite, self).checkout_form_validate(mode=mode,
                                                                  all_form_values=all_form_values,
                                                                  data=data)
        error = res[0]
        error_message = res[1]

        # get api authentication parameter from website configuration
        auth_id = request.env['ir.config_parameter'].sudo().get_param('address_verification.auth_id')
        auth_token = request.env['ir.config_parameter'].sudo().get_param('address_verification.auth_token')

        # check if there api credential , make api client , send data and receive response
        if auth_id and auth_token:
            client = Client(auth_id, auth_token, standardize=True, invalid=False,
                            logging=False)
            address = client.street_address({
                'input_id': data.get('partner_id'),
                'city': data.get('city'),
                'street': data.get('street'),
                'state': data.get('state'),
                'zipcode': data.get('zip'),
            })

            if address is None:
                if address.city != data.get('city') and address.zipcode != data.get('zip'):
                    error_message.append(_('Please check City and zip code!'))

            elif address is not None:
                error_message.append(_('Address is seem Valid'))



        else:
            raise ValidationError(_("you Must Enter Auth ID and Token at Configuration Fist"))

        return res
