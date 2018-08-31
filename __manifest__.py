# -*- coding: utf-8 -*-
{
    'name': "Giathuochapu website",

    'summary': """
        New website for https://giathuochapu.com, use odoo11, base on website_sale (odoo ecommerce) module""",

    'description': """
        New website for giathuochapu.com, use odoo11, base on website_sale (odoo ecommerce) module
    """,

    'author': "Entrust company",
    'website': "http://entrustlab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'website_blog', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead.xml',
        'views/assets.xml',
        'views/views.xml',
        'views/address_book_template.xml',
        'views/config_new.xml',
        'views/templates.xml',
        'views/page/homepage.xml',
        'views/page/blog_post_inherit.xml',
        'views/page/blog_post_template_inherit.xml',
        'views/page/contact_us.xml',
        'views/page/introduce.xml',
        'views/page/custom_website_blog.xml',
        'views/page/res_partner_inherit.xml',
        'views/page/custom_account.xml',
        'views/components.xml',
        'views/snippets.xml',
    ],
}
