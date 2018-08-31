from odoo import api, fields, models
from odoo.addons.portal.controllers.portal import pager

class WebsiteInherit (models.Model):

    _inherit = "website"
    _description = "Website"

    @api.model
    def pager(self, url, total, page=1, step=30, scope=5, url_args=None):
        data = pager(url, total, page=page, step=step, scope=scope, url_args=url_args)
        data['base_url'] = url
        data['url_args'] = url_args
        return data