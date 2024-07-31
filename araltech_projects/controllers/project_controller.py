from odoo import http
from odoo.http import request

class ProjectController(http.Controller):

    @http.route('/projects', type='http', auth='public', website=True)
    def project_list(self, **kwargs):
        projects = request.env['araltech.project'].search([])
        return request.render('araltech_projects.project_list_template', {'projects': projects})

    @http.route('/projects/<model("araltech.project"):project>', type='http', auth='public', website=True)
    def project_detail(self, project, **kwargs):
        return request.render('araltech_projects.project_detail_template', {'project': project})
