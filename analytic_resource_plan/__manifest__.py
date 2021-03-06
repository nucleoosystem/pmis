# -*- coding: utf-8 -*-
#    Copyright 2016 MATMOZ, Slovenia (Matjaž Mozetič)
#    Copyright 2018 EFICENT (Jordi Ballester Alomar)
#    Copyright 2018 LUXIM, Slovenia (Matjaž Mozetič)
#    Together as the Project Expert Team
#    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Analytic Resource Planning',
    'version': '10.0.1.0.0',
    'category': 'Advanced Project Management',
    'license': 'AGPL-3',
    'summary': 'Analytic resource cost planning',
    'website': 'https://github.com/projectexpert',
    'author': 'Eficent, '
              'Luxim, '
              'Project Expert Team',
    # 'author': 'Eficent, '
    #           'Luxim, '
    #           'Odoo Community Association (OCA)',
    # 'website': 'https://github.com/OCA/...',
    'contributors': [
        'Matjaž Mozetič <matjaz@luxim.si>',
        'Jordi Ballester <jordi.ballester@eficent.com>',
    ],
    'depends': [
        'account',
        'purchase',
        'analytic_plan'
    ],
    'data': [
        'security/ir.model.access.csv',
        'view/account_analytic_plan_version_view.xml',
        'view/account_analytic_line_plan_view.xml',
        'view/analytic_resource_plan_view.xml',
        'view/analytic_account_view.xml',
        'view/project_view.xml',
        'view/resource_plan_default.xml',
        'wizard/analytic_resource_plan_copy_version_view.xml',
        'wizard/resource_plan_line_change_state_view.xml',
    ],
    'installable': True,
}
