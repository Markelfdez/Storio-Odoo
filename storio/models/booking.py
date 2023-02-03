# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Booking(models.Model):
    _name = 'storio.booking'
    
    id = fields.Integer(string = "ID", required = True)
    description = fields.Text(string = "Description", required = True)
    endDate = fields.Date(string="End date", default=fields.Date.from_string(fields.Date.today()), required = True)
    startDate = fields.Date(string = "Start date", default=fields.Date.from_string(fields.Date.today()), required = True)
    #user = fields.One2many('res.users', string = "User", required = True)
    packs = fields.Many2many('storio.pack', string = "Packs", required = True)
    state = fields.Selection([("pending","PENDING"),("approved","APROVED"),("handed","HANDED"),("returned","RETURNED"),("denied","DENIED")], string = "State")


            
            
            
            
    @api.constrains('endDate')
    def _constrains_date(self):
        for task in self:
            if fields.Date.from_string(task.endDate) < fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be greater than today date.")

    @api.onchange('endDate')
    def _onchange_date(self):
        if fields.Date.from_string(self.endDate) < fields.Date.from_string(fields.Date.today()):
            return{
                'warning':{
                    'title': "Date incorrect",
                    'message': "Date cannot be greater than today date.",
                },
            }