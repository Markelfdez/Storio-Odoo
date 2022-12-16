from odoo import models, fields, api


class client(models.user):

    _name = 'storio.client'

    bookings = fields.One2many('storio.booking', 'booking_id', string='Client Bookings')
