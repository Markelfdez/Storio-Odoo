# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class pack(models.Model):
    _name = 'storio.pack'
    
    name = fields.Char()
    
    id = fields.Integer(string="Id", required=True)
    description = fields.Text(string="Description")
    datePackAdd = fields.Date(string="Date Pack Added", required=True)
    packState = fields.Selection(selection=[('Available', 'Available'), ('Unavailable', 'Unavailable')], string='Pack state', required=True)
    packType = fields.Selection(selection=[
                                ('Sound', 'Sound'), 
                                ('Lighting', 'Lighting'), 
                                ('Camera', 'Camera'), 
                                ('Tripod', 'Tripod'),
                                ('Special', 'Special')],
                                string='Pack type', required=True)
    items = fields.One2many('storio.item', 'pack', string="Items")
    bookings = fields.Many2many('storio.booking', string="Bookings")

    @api.onchange('description')
    def _onchange_description(self):
        if self.description:
            if len(self.description) < 10:
                return {
                    'warning': {
                        'title': "Incorrect 'description' value",
                        'message': "value should atleast be 10 characters long"
                    }
                }

    @api.multi
    @api.constrains('name')
    def _check_correct_name(self):
        for r in self:
            if len(self.name) < 5:
                raise ValidationError("Name is not valid")