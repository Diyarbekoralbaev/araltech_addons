{
    'name': 'AralTech Projects',
    'version': '1.0',
    'summary': 'Manage and Display Projects on Website',
    'description': 'Module to manage projects and display them dynamically on the website.',
    'category': 'Website',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'depends': ['base', 'website'],
    'data': [
        'security/public.xml',
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/project_templates.xml',  # Ensure this is included
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
