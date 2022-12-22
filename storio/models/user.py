from odoo import models, fields, api


class user(models.Model):

    _inherit = 'res.users'

    status = fields.Selection(
        [('ENABLED', 'ENABLED'),
            ('DISABLED', 'DISABLED')],
        string='User Status')

    privilege = fields.Selection(
        [('ADMIN', 'ADMIN'),
            ('USER', 'USER'),
            ('MANAGER', 'MANAGER')],
        string='User Privilege'
    )

    phoneNumber = fields.Integer(string='Phone Number', required=True)
