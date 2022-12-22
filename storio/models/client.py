from odoo import models, fields, api


class client(models.Model):

    _inherit = 'storio.user'

    bookings = fields.One2many('storio.booking', 'booking_id', string='Client Bookings')
