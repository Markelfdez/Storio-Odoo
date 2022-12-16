# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Report(models.Model):
     _name = 'storio.report'

     name = fields.Char()
     
     id = fields.Integer(string="ID")
     date = fields.Date(string="Date")
     description = fields.Text(string="Description")
     item = fields.One2Many('storio.item')
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100