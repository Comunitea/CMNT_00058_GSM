# -*- coding: utf-8 -*-
# © 2016 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.model
    def create(self, vals):
        res = super(AccountInvoice, self).create(vals)
        res.button_reset_taxes()

        return res
