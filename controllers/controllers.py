# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteHapu(http.Controller):
#     @http.route('/website_hapu/website_hapu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_hapu/website_hapu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_hapu.listing', {
#             'root': '/website_hapu/website_hapu',
#             'objects': http.request.env['website_hapu.website_hapu'].search([]),
#         })

#     @http.route('/website_hapu/website_hapu/objects/<model("website_hapu.website_hapu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_hapu.object', {
#             'object': obj
#         })