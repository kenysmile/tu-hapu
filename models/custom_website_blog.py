# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CustomWebsiteBlogPost(models.Model):
    _inherit = 'blog.post'
    sequence = fields.Integer(default=0)
    image = fields.Binary(string='Upload Image')
    # content = fields.Html(string='Nội dung')
