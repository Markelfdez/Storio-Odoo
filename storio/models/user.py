from odoo import models, fields, api


class user(models.Model):

    _name = 'storio.user'

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

    login = fields.Char(string='login', required=True)

    phoneNumber = fields.Integer(string='Phone Number', required=True)

    fullName = fields.Char(string='Full Name', required=True)

    password = fields.Char(string='Password', required=True, password=True)

    email = fields.Char(string='Email', required=True)

    history = fields.One2many('storio.signinhistory', 'history_id', string='Sign In History')
