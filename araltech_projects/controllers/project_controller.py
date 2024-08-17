from odoo import http
from odoo.http import request


class ProjectController(http.Controller):

    @http.route('/projects', type='http', auth='public', website=True)
    def project_list(self, **kwargs):
        projects = request.env['araltech.project'].sudo().search([('status', '=', True)])
        return request.render('araltech_projects.project_list_template', {'projects': projects})

    @http.route('/projects/<int:project_id>', type='http', auth='public', website=True)
    def project_detail(self, project_id, **kwargs):
        project = request.env['araltech.project'].sudo().browse(project_id)
        if not project:
            return request.not_found()
        if not project.status:
            return request.not_found()
        return request.render('araltech_projects.project_detail_template', {'project': project})
