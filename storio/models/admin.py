from odoo import models, fields, api


class admin(models.user):

    _name = 'storio.admin'

    isSuperAdmin = fields.Boolean(string='Is Super Admin', required=True)
