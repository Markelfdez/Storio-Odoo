# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Model(models.Model):
	_name = 'storio.model'

	name = fields.Char()
     
	id = fields.Integer(string="ID", required=True)

	model = fields.Char(string="Model", required=True)

	notes = fields.Text(string="Notes")

	description = fields.Text(string="Description", required=True)

	item_ids = fields.One2many('storio.item', 'model_id', string="Items")
     
	@api.onchange('description')
	def _onchange_description(self):
		if self.description:
			if len(self.description) < 10:
				return {
					'warning': {
						'title': "Incorrect 'description' value",
						'message': self.description + ": value should atleast be 10 characters long"
					}
				}
