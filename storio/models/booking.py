# -*- coding: utf-8 -*-

from odoo import models, fields

class Booking(models.Model):
    _name = 'storio.booking'
    
    id = fields.Integer(string = "ID", required = true)
    description = fields.Text(string = "Description", required = true)
    endDate = fields.Date(string="End date", required = true)
    startDate = fields.Date(string = "Start date", required = true)
    user = fields.One2many(string = "User", required = true)
    packs = fields.Many2many(string = "Packs", required = true)
    state = fields.Selection([("pending","PENDING"),("approved","APROVED"),("handed","HANDED"),("returned","RETURNED"),("denied","DENIED")], string = "State")
    

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100