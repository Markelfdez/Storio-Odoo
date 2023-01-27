# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Model(models.Model):
	_name = 'storio.model'

	name = fields.Char(string="Name", required=True)
     
	id = fields.Integer(string="ID", required=True)

	model = fields.Char(string="Model", required=True)

	notes = fields.Text(string="Notes")

	description = fields.Text(string="Description", required=True)

	items = fields.One2many('storio.item', 'model', string="Items")

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

	@api.multi
	@api.constrains('model')
	def _check_if_model_exists(self):
		modelObj = self.env['storio.model']
		for record in self:
			rec = modelObj.search([('model', '=', record.model)])
			if rec:
				raise ValidationError("This Model exists already! Model: %s" % record.model)

