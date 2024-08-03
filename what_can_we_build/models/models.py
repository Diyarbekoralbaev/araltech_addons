# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ServiceCategory(models.Model):
    _name = 'what_can_we_build.service_category'
    _description = 'Service Category'

    name = fields.Char(string='Name', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], string='Status', default='draft')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)


class Service(models.Model):
    _name = 'what_can_we_build.service'
    _description = 'Service'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    features = fields.Text(string='Features')
    image = fields.Binary(string='Image')
    price = fields.Float(string='Price')
    duration = fields.Integer(string='Duration')
    category = fields.Many2one('what_can_we_build.service_category', string='Category')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], string='Status', default='draft')
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        vals['created_at'] = fields.Datetime.now()
        vals['updated_at'] = fields.Datetime.now()
        return super(Service, self).create(vals)

    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super(Service, self).write(vals)
