# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WhatCanWeBuild(http.Controller):

    @http.route('/what_can_we_build', type='http', auth='public', website=True)
    def services_page(self):
        services = request.env['what_can_we_build.service'].sudo().search([('status', '=', 'published')])
        return request.render('what_can_we_build.services_page', {
            'services': services
        })
