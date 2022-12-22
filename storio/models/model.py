# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Model(models.Model):
     _name = 'storio.model'

     name = fields.Char()
     
     id = fields.Integer(string="ID")
     model = fields.Char(string="Model")
     notes = fields.Text(string="Notes")
     description = fields.Text(string="Description")
     items = fields.One2many('storio.item')
     
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100