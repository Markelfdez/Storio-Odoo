from odoo import models, fields, api


class signinhistory(models.Model):

    _name = 'storio.signinhistory'

    user = fields.Many2one('storio.user', 'user_id', string='User')

    lastSignIn = fields.Date(string='Last SignIn')
