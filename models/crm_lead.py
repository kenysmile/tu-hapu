# -*- coding: utf-8 -*-

from odoo import models, fields

class website_hapu(models.Model):
    _inherit = "crm.lead"

    company_type = fields.Selection(string='Company Type',
                                    selection=[('person', 'Individual'), ('company', 'Company'),])