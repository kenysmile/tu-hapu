# -*- coding: utf-8 -*-

from odoo.http import Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortalInh(CustomerPortal):
    MANDATORY_BILLING_FIELDS = ["name"]
    OPTIONAL_BILLING_FIELDS = ["phone", "email", "dateofbird", "drugstore_name"]
