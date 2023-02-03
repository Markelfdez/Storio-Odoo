# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Item(models.Model):
    _name = 'storio.item'

    name = fields.Char(default="Unknown", required=True)
     
    iden = fields.Integer(string="ID", required=True, default="1")
    issues = fields.Text(string="Issues", default="No issues.")
    dateAdded = fields.Date(string="Date Added", required=True, default=fields.Date.today)
    model_id = fields.Many2one('storio.model', string="Model", required=True)
    pack = fields.Many2one("storio.pack", string="Pack")
     
    @api.onchange('iden')
    def _onchange_iden(self):
        if self.iden <= 0:
            
            return {
                'warning': {
                    'title': "Incorrect ID value",
                    'message': "ID cannot be negative.",
                }
            }   
            
    @api.constrains('iden')
    def _constrains_iden(self):
        if self.iden <= 0:
            
            raise exceptions.ValidationError("ID MAL.")
