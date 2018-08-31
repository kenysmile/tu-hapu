# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class AddressBook(http.Controller):
    @http.route('/account_info/address_book/', auth='user', method=['POST'], type="http", website=True)
    def address_book(self, **kw):
        if request.httprequest.method == 'POST':
            values = {
                "name": kw.get("name"),
                "phone": kw.get("phone"),
                "email": kw.get("email"),
                "state_id": kw.get("state_id"),
                "street": kw.get("street"),
                "type": "delivery",
                "parent_id": request.env.user.partner_id.id,
            }
            create_book = request.env["res.partner"].sudo().create(values)
            if create_book and kw.get('default_id'):
                request.env.user.partner_id.default_id = create_book.id

        states = request.env['res.country.state'].sudo().search([])
        Partner = request.env['res.partner'].with_context(show_address=1).sudo()
        product_context = dict(request.env.context, partner=request.env.user.partner_id)
        partners = Partner.search([('id', 'child_of', product_context['partner'].commercial_partner_id.ids)])
        return http.request.render('website_hapu.address_book',
                                   {'partners': partners, 'states': states, 'default_id': request.env.user.partner_id.default_id})

class RemoveAddressBook(http.Controller):
    @http.route('/account_info/address_book/remove_book/<int:id>', auth='user', type="http", website=True)
    def remove_address_book(self, id):
        if request.httprequest.method == 'POST':
            partner_id = request.env['res.partner'].sudo().browse(id)
            partner_id.unlink()
        return http.request.redirect('/account_info/address_book/')

class EditAddressBook(http.Controller):
    @http.route(['/account_info/address_book/edit_book/<int:id>'], auth='user', type="http", website=True)
    def edit_address_book(self, id, **kw):
        if request.httprequest.method == 'POST':
            values = {
                "id": id,
                "name": kw.get("name"),
                "phone": kw.get("phone"),
                "email": kw.get("email"),
                "state_id": kw.get("state_id"),
                "street": kw.get("street"),
                "type": "delivery",
            }
            edit_book = request.env["res.partner"].sudo().browse(id).write(values)
            if edit_book and kw.get('default_id'):
                request.env.user.partner_id.default_id = id
            else:
                request.env.user.partner_id.default_id == None

        return http.request.redirect('/account_info/address_book/')