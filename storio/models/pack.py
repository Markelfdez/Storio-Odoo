# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class pack(models.Model):
    _name = 'storio.pack'
    
    name = fields.Char()
    
    id = fields.Integer(string="Id", required=True)
    description = fields.Text(string="Description")
    datePackAdd = fields.Date(string="Date Pack Added",required=True)
    packState = fields.Selection(selection=[('Available', 'Available'), ('Unavailable', 'Unavailable')],string='Pack state')
    packType = fields.Selection(selection=[
                                    ('Sound', 'Sound'), 
                                    ('Lighting', 'Lighting'), 
                                    ('Camera', 'Camera'), 
                                    ('Tripod', 'Tripod'),
                                    ('Special', 'Special')],
                                    string='Pack type')
    #items = fields.One2many('storio.item', 'pack', string="Items")
    bookings = fields.Many2Many('storio.booking', string="Bookings")
