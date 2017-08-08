# -*- coding: utf-8 -*-
from odoo import http

# class Hrskill(http.Controller):
#     @http.route('/hrskill/hrskill/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hrskill/hrskill/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hrskill.listing', {
#             'root': '/hrskill/hrskill',
#             'objects': http.request.env['hrskill.hrskill'].search([]),
#         })

#     @http.route('/hrskill/hrskill/objects/<model("hrskill.hrskill"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hrskill.object', {
#             'object': obj
#         })