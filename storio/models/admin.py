from odoo import models, fields, api


class admin(models.Model):

    _inherit = 'storio.user'

    isSuperAdmin = fields.Boolean(string='Is Super Admin', required=True)
