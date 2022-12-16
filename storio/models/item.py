# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Item(models.Model):
     _name = 'storio.item'

     name = fields.Char()
     
     id = fields.Integer(string="ID", required=True)
     issues = fields.Text(string="Issues")
     dateAdded = fields.Date(string="Date Added",required=True)
     model = fields.One2Many('storio.model')
     pack = fields.One2Many('storio.pack')
     report = fields.Many2One('storio.report')
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100