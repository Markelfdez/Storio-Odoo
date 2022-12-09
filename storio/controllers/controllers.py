# -*- coding: utf-8 -*-
from odoo import http

# class Storio(http.Controller):
#     @http.route('/storio/storio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/storio/storio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('storio.listing', {
#             'root': '/storio/storio',
#             'objects': http.request.env['storio.storio'].search([]),
#         })

#     @http.route('/storio/storio/objects/<model("storio.storio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('storio.object', {
#             'object': obj
#         })