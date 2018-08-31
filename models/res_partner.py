# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    dateofbird = fields.Date(string="Ngày sinh")
    x_business_format = fields.Selection([
        ('drugstore', 'Nhà thuốc'),
        ('drugstores', 'Quầy thuốc'),
        ('clinic', 'Phòng khám'),
        ('pharmaceutical_representatives', 'Trình dược viên'),
    ], default="drugstore", string="Hình thức kinh doanh")
    drugstore_name = fields.Char(string="Tên nhà thuốc")
    default_id = fields.Many2one('res.partner', string='Địa chỉ mặc định')
