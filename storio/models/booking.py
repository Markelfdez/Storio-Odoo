# -*- coding: utf-8 -*-

from odoo import models, fields

class Booking(models.Model):
    _name = 'storio.booking'
    
    id = fields.Integer(string = "ID", required = True)
    description = fields.Text(string = "Description", required = True)
    endDate = fields.Date(string="End date", required = True)
    startDate = fields.Date(string = "Start date", required = True)
    user = fields.One2many('res.users', string = "User", required = True)
    packs = fields.Many2Many('storio.pack', string = "Packs", required = True)
    state = fields.Selection([("pending","PENDING"),("approved","APROVED"),("handed","HANDED"),("returned","RETURNED"),("denied","DENIED")], string = "State")
