# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.http import request


class CustomHomepage(models.Model):
    _inherit = 'website'

    def get_blog(self):
        return self.env['blog.post'].search([])

    def get_blog_category(self):
        return self.env['blog.blog'].search([])

    def get_sale_order_login_user(self):
        login_user_id = request.env.user.id if request.env.user.id else ''
        return self.env['sale.order'].search([('user_id.id', '=', login_user_id)])