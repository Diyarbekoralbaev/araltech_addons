# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Project(models.Model):
    _name = 'araltech.project'
    _description = 'Project'

    name = fields.Char(string="Name", required=True, translate=True)
    description = fields.Html(string="Description" , translate=True)
    image = fields.Binary(string="Image", attachment=True , help="This field holds the image used as image for the project, limited to 1024x1024px.")
    demo_url = fields.Char(string="Demo URL" , help="This field holds the URL of the demo for the project.")
    demo_video_url = fields.Char(string="Demo Video URL" , help="This field holds the URL of the demo video for the project.")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    @api.model
    def create(self, vals):
        """Override the create method to add custom logic."""
        # Add any custom logic before creation
        project = super(Project, self).create(vals)
        # Add any custom logic after creation
        return project

    def write(self, vals):
        """Override the write method to add custom logic."""
        # Add any custom logic before writing
        result = super(Project, self).write(vals)
        # Add any custom logic after writing
        return result

    def unlink(self):
        """Override the unlink method to add custom logic."""
        for record in self:
            # Add any custom logic before deletion
            pass
        result = super(Project, self).unlink()
        # Add any custom logic after deletion
        return result

    @api.model
    def update_project_dates(self, project_id, start_date, end_date):
        """Custom method to update the project dates."""
        project = self.browse(project_id)
        project.write({
            'start_date': start_date,
            'end_date': end_date
        })

    @api.model
    def get_projects_by_date_range(self, start_date, end_date):
        """Custom method to fetch projects within a specific date range."""
        return self.search([('start_date', '>=', start_date), ('end_date', '<=', end_date)])